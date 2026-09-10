import sqlite3
import requests
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from espn_stats_fetcher import get_espn_player_stats
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
import zoneinfo

DB_PATH = os.path.join(BASE_DIR, "bdl_data.db")

TEAM_NAME_MAP = {
    "Bayern Munich": "바이에른 뮌헨", "FC Bayern München": "바이에른 뮌헨", "FC Bayern Munich": "바이에른 뮌헨",
    "Bayer Leverkusen": "바이어 레버쿠젠", "Bayer 04 Leverkusen": "바이어 레버쿠젠",
    "Borussia Dortmund": "보루시아 도르트문트", "Dortmund": "보루시아 도르트문트",
    "RB Leipzig": "RB 라이프치히", "Leipzig": "RB 라이프치히",
    "Eintracht Frankfurt": "아인트라흐트 프랑크푸르트", "Frankfurt": "아인트라흐트 프랑크푸르트",
    "VfB Stuttgart": "슈투트가르트", "Stuttgart": "슈투트가르트",
    "VfL Wolfsburg": "볼프스부르크", "Wolfsburg": "볼프스부르크",
    "Borussia Mönchengladbach": "보루시아 묀헨글라트바흐", "Mönchengladbach": "보루시아 묀헨글라트바흐",
    "TSG Hoffenheim": "호펜하임", "TSG 1899 Hoffenheim": "호펜하임", "Hoffenheim": "호펜하임",
    "SC Freiburg": "프라이부르크", "Freiburg": "프라이부르크",
    "FC Augsburg": "아우크스부르크", "Augsburg": "아우크스부르크",
    "Mainz": "마인츠 05", "Mainz 05": "마인츠 05", "FSV Mainz 05": "마인츠 05",
    "Werder Bremen": "베르더 브레멘", "SV Werder Bremen": "베르더 브레멘", "Bremen": "베르더 브레멘",
    "1. FC Union Berlin": "우니온 베를린", "Union Berlin": "우니온 베를린",
    "St. Pauli": "장크트파울리", "FC St. Pauli": "장크트파울리",
    "Holstein Kiel": "홀슈타인 킬", "Kiel": "홀슈타인 킬",
    "VfL Bochum": "보훔", "Bochum": "보훔",
    "1. FC Heidenheim 1846": "하이덴하임", "FC Heidenheim": "하이덴하임", "Heidenheim": "하이덴하임",
    "FC Cologne": "쾰른", "1. FC Köln": "쾰른", "Hamburg SV": "함부르크",
    "SV Elversberg": "엘버스베르크", "SC Paderborn 07": "파더보른", "Schalke 04": "샬케 04", "FC Schalke 04": "샬케 04"
}

def normalize_team_name(raw_name):
    if not raw_name:
        return raw_name
    for key, val in TEAM_NAME_MAP.items():
        if key.lower() in raw_name.lower() or raw_name.lower() in key.lower():
            return val
    return raw_name

def get_team_roster(team_name, absentees=None):
    rosters_path = os.path.join(BASE_DIR, "rosters_2026.json")
    if not os.path.exists(rosters_path):
        return {"starters": [], "subs": []}
    with open(rosters_path, "r", encoding="utf-8") as f:
        rosters = json.load(f)
        
    normalized_map = {normalize_team_name(k): v for k, v in rosters.items()}
    norm_tname = normalize_team_name(team_name)
    plist = normalized_map.get(norm_tname, [])
    
    if absentees is None:
        absentees = []
        
    available = [p for p in plist if p.get("name") not in absentees]
    
    for p in available:
        p["calc_uv"] = calculate_player_uv(p, team_name)
        
    gks = sorted([p for p in available if p.get("pos") in ["G", "GK"]], key=lambda x: x["calc_uv"], reverse=True)
    dfs = sorted([p for p in available if p.get("pos") in ["D", "DF"]], key=lambda x: x["calc_uv"], reverse=True)
    mfs = sorted([p for p in available if p.get("pos") in ["M", "MF"]], key=lambda x: x["calc_uv"], reverse=True)
    fws = sorted([p for p in available if p.get("pos") in ["F", "FW"]], key=lambda x: x["calc_uv"], reverse=True)
    
    starters = gks[:1] + dfs[:4] + mfs[:3] + fws[:3]
    subs = (gks[1:2] + dfs[4:6] + mfs[3:5] + fws[3:5])[:5]
    return {"starters": starters, "subs": subs}

def calculate_player_uv(player_data, team_name=""):
    p_name_raw = player_data.get("name", "")
    
    rating = None
    goals_per90 = 0.0
    position = player_data.get("pos", "MF")
    
    espn_res = get_espn_player_stats(p_name_raw)
    if espn_res:
        rating, goals_per90 = espn_res
        
    pos_clean = "GK" if position in ["G", "GK"] else ("DF" if position in ["D", "DF"] else ("MF" if position in ["M", "MF"] else "FW"))
    
    if rating is None or rating == 0:
        if pos_clean == "GK":
            raw_uv = 0.95
        elif pos_clean == "DF":
            raw_uv = 0.90
        elif pos_clean == "MF":
            raw_uv = 0.88
        else:
            raw_uv = 0.85
    elif rating >= 6.88:
        if pos_clean in ["GK", "DF", "MF"]:
            raw_uv = 1.0 + (rating - 6.88) * 0.50
        else: # FW
            raw_uv = 1.0 + (rating - 6.88) * 0.50 + (goals_per90 * 0.40)
    else:
        slope = 0.80 if pos_clean == "MF" else 0.65
        raw_uv = 1.0 + (rating - 6.88) * slope + (goals_per90 * 0.40 if pos_clean == "FW" else 0.0)
        
    return round(min(max(raw_uv, 0.1), 2.5), 3)

def calculate_wuv(team_name, absentees=None):
    roster = get_team_roster(team_name, absentees=absentees)
    starters = roster.get("starters", [])
    subs = roster.get("subs", [])
    
    st_uvs = [calculate_player_uv(p, team_name) for p in starters]
    sub_uvs = [calculate_player_uv(p, team_name) for p in subs]
    
    st_avg = sum(st_uvs) / len(st_uvs) if st_uvs else 0.95
    sub_avg = sum(sub_uvs) / len(sub_uvs) if sub_uvs else 0.85
    
    st_tot_sum = sum(st_uvs)
    sub_tot_sum = sum(sub_uvs)
    raw_wuv = 0.85 * st_avg + 0.15 * sub_avg
    team_wuv = round(raw_wuv * 11.0, 3)
    
    pos_sums = {"GK": 0.0, "DF": 0.0, "MF": 0.0, "FW": 0.0}
    starters_detail = []
    for p in starters:
        uv = calculate_player_uv(p, team_name)
        pos = p.get("pos", "M")
        pos_clean = "GK" if pos in ["G","GK"] else ("DF" if pos in ["D","DF"] else ("MF" if pos in ["M","MF"] else "FW"))
        pos_sums[pos_clean] += uv
        starters_detail.append({"name": p.get("name"), "pos": pos_clean, "uv": uv})
        
    tot_st_uv = sum(pos_sums.values()) or 1.0
    gk_wuv = round(team_wuv * (pos_sums["GK"] / tot_st_uv), 2)
    df_wuv = round(team_wuv * (pos_sums["DF"] / tot_st_uv), 2)
    mf_wuv = round(team_wuv * (pos_sums["MF"] / tot_st_uv), 2)
    fw_wuv = round(team_wuv * (pos_sums["FW"] / tot_st_uv), 2)
    
    return {
        "team_wuv": team_wuv,
        "st_avg": round(st_avg, 3),
        "sub_avg": round(sub_avg, 3),
        "st_sum": round(st_tot_sum, 3),
        "sub_sum": round(sub_tot_sum, 3),
        "gk_wuv": gk_wuv,
        "df_wuv": df_wuv,
        "mf_wuv": mf_wuv,
        "fw_wuv": fw_wuv,
        "starters": starters_detail
    }

def get_match_prediction(home_team, away_team):
    h_info = calculate_wuv(home_team)
    a_info = calculate_wuv(away_team)
    
    h_total = h_info["team_wuv"] + 0.15
    a_total = a_info["team_wuv"]
    
    gap = h_total - a_total
    
    home_kr = TEAM_NAME_MAP.get(home_team, home_team)
    away_kr = TEAM_NAME_MAP.get(away_team, away_team)
    
    if abs(gap) <= 0.40:
        winner = "무승부"
        code = "DRAW"
    elif gap > 0.40:
        winner = f"{home_kr} 승"
        code = "HOME"
    else:
        winner = f"{away_kr} 승"
        code = "AWAY"
        
    z = gap
    lh = 1.55 * z
    la = -1.55 * z
    ld = 0.35 - 1.25 * abs(z)
    
    eh, ed, ea = np.exp(lh), np.exp(ld), np.exp(la)
    tot = eh + ed + ea
    
    p_home = round((eh / tot) * 100, 1)
    p_draw = round((ed / tot) * 100, 1)
    p_away = round((ea / tot) * 100, 1)
    
    sc_h = int(round(1.35 * (h_total / 11.0)))
    sc_a = int(round(1.35 * (a_total / 11.0)))
    
    if code == "DRAW":
        sc_h = sc_a = int(round((sc_h + sc_a) / 2.0))
    elif code == "HOME" and sc_h <= sc_a:
        sc_h = sc_a + 1
    elif code == "AWAY" and sc_a <= sc_h:
        sc_a = sc_h + 1
        
    return {
        "home_wuv": h_info,
        "away_wuv": a_info,
        "h_total": h_total,
        "a_total": a_total,
        "gap": gap,
        "winner": winner,
        "code": code,
        "p_home": p_home,
        "p_draw": p_draw,
        "p_away": p_away,
        "sc_h": sc_h,
        "sc_a": sc_a
    }

def run_pipeline(mode="all"):
    url = "https://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/scoreboard?dates=20260801-20270601&limit=500"
    
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            print(f"⚠️ ESPN API HTTP error: {res.status_code}")
            return
        events = res.json().get("events", [])
    except Exception as e:
        print(f"⚠️ ESPN API 요청 오류: {e}")
        return

    if not events:
        print("⚠️ 분데스리가 경기 데이터가 없습니다.")
        return

    events.sort(key=lambda x: x["date"])

    matchweeks = []
    chunk_size = 9
    for i in range(0, len(events), chunk_size):
        matchweeks.append(events[i:i + chunk_size])

    print(f"2026/27 시즌 총 {len(matchweeks)}개 라운드(Gameweek 1 ~ Gameweek {len(matchweeks)}) 수집됨.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id TEXT UNIQUE,
        round_name TEXT NOT NULL,
        home_team TEXT NOT NULL,
        away_team TEXT NOT NULL,
        match_date TEXT NOT NULL,
        match_date_ger TEXT NOT NULL,
        match_date_kst TEXT NOT NULL,
        home_wuv REAL NOT NULL,
        away_wuv REAL NOT NULL,
        home_total_wuv REAL NOT NULL,
        away_total_wuv REAL NOT NULL,
        gap REAL NOT NULL,
        predicted_winner TEXT NOT NULL,
        prob_home REAL NOT NULL,
        prob_draw REAL NOT NULL,
        prob_away REAL NOT NULL,
        score_home INTEGER NOT NULL,
        score_away INTEGER NOT NULL,
        actual_score_home INTEGER,
        actual_score_away INTEGER,
        actual_winner TEXT,
        is_correct INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    ger_tz = zoneinfo.ZoneInfo("Europe/Berlin")
    kst_tz = zoneinfo.ZoneInfo("Asia/Seoul")

    for mw_idx, mw_events in enumerate(matchweeks, 1):
        round_label = f"Round {mw_idx} (Gameweek {mw_idx})"
        mw_prefix = f"GW{mw_idx}"
        
        for game_idx, e in enumerate(mw_events, 1):
            comp = e.get("competitions", [{}])[0]
            competitors = comp.get("competitors", [])
            if len(competitors) < 2:
                continue
                
            home_comp = competitors[0] if competitors[0].get("homeAway") == "home" else competitors[1]
            away_comp = competitors[1] if competitors[0].get("homeAway") == "home" else competitors[0]
            
            h_team_raw = home_comp.get("team", {}).get("displayName", "")
            a_team_raw = away_comp.get("team", {}).get("displayName", "")
            
            h_team = normalize_team_name(h_team_raw)
            a_team = normalize_team_name(a_team_raw)
            
            date_raw = e.get("date", "")
            if date_raw:
                dt_utc = datetime.fromisoformat(date_raw.replace("Z", "+00:00"))
                dt_ger = dt_utc.astimezone(ger_tz)
                dt_kst = dt_utc.astimezone(kst_tz)
                ger_date_str = dt_ger.strftime("%Y-%m-%d")
                kst_date_str = dt_kst.strftime("%Y-%m-%d")
            else:
                ger_date_str = "2026-08-28"
                kst_date_str = "2026-08-29"

            status_type = e.get("status", {}).get("type", {}).get("name", "")
            is_completed = (status_type == "STATUS_FULL_TIME")
            is_cancelled = status_type in ["STATUS_POSTPONED", "STATUS_CANCELED", "STATUS_SUSPENDED", "STATUS_ABANDONED"]
            
            act_sc_h = int(home_comp.get("score")) if (is_completed and home_comp.get("score") is not None) else None
            act_sc_a = int(away_comp.get("score")) if (is_completed and away_comp.get("score") is not None) else None
            
            if is_completed and act_sc_h is not None and act_sc_a is not None:
                if act_sc_h > act_sc_a:
                    act_winner = f"{h_team} 승"
                elif act_sc_a > act_sc_h:
                    act_winner = f"{a_team} 승"
                else:
                    act_winner = "무승부"
            elif is_cancelled:
                act_winner = "경기 연기"
            else:
                act_winner = None
                
            mid = f"2026_{mw_prefix}_{game_idx}"
            
            cursor.execute("SELECT predicted_winner FROM predictions WHERE match_id = ?", (mid,))
            existing = cursor.fetchone()
            
            if existing:
                pred_winner = existing[0]
                if mode in ["score", "all"]:
                    if is_completed and act_winner is not None:
                        if (act_winner == pred_winner) or (h_team in act_winner and h_team in pred_winner) or (a_team in act_winner and a_team in pred_winner):
                            is_corr = 1
                        else:
                            is_corr = 0
                    else:
                        is_corr = None
                        
                    cursor.execute("""
                    UPDATE predictions SET
                        match_date_ger = ?,
                        match_date_kst = ?,
                        actual_score_home = ?,
                        actual_score_away = ?,
                        actual_winner = ?,
                        is_correct = ?
                    WHERE match_id = ?
                    """, (ger_date_str, kst_date_str, act_sc_h, act_sc_a, act_winner, is_corr, mid))
                
                if mode in ["predict", "all"]:
                    pred = get_match_prediction(h_team, a_team)
                    pred_winner = pred["winner"]
                    cursor.execute("""
                    UPDATE predictions SET
                        home_wuv = ?, away_wuv = ?, home_total_wuv = ?, away_total_wuv = ?,
                        gap = ?, predicted_winner = ?, prob_home = ?, prob_draw = ?, prob_away = ?,
                        score_home = ?, score_away = ?
                    WHERE match_id = ?
                    """, (
                        pred["home_wuv"]["team_wuv"], pred["away_wuv"]["team_wuv"], pred["h_total"], pred["a_total"],
                        pred["gap"], pred_winner, pred["p_home"], pred["p_draw"], pred["p_away"],
                        pred["sc_h"], pred["sc_a"], mid
                    ))
            else:
                pred = get_match_prediction(h_team, a_team)
                pred_winner = pred["winner"]
                
                if is_completed and act_winner is not None:
                    if (act_winner == pred_winner) or (h_team in act_winner and h_team in pred_winner) or (a_team in act_winner and a_team in pred_winner):
                        is_corr = 1
                    else:
                        is_corr = 0
                else:
                    is_corr = None
                    
                cursor.execute("""
                INSERT INTO predictions (
                    match_id, round_name, home_team, away_team, match_date, match_date_ger, match_date_kst,
                    home_wuv, away_wuv, home_total_wuv, away_total_wuv,
                    gap, predicted_winner, prob_home, prob_draw, prob_away,
                    score_home, score_away,
                    actual_score_home, actual_score_away, actual_winner, is_correct
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    mid, round_label, h_team, a_team, ger_date_str, ger_date_str, kst_date_str,
                    pred["home_wuv"]["team_wuv"], pred["away_wuv"]["team_wuv"], pred["h_total"], pred["a_total"],
                    pred["gap"], pred_winner, pred["p_home"], pred["p_draw"], pred["p_away"],
                    pred["sc_h"], pred["sc_a"],
                    act_sc_h, act_sc_a, act_winner, is_corr
                ))

    conn.commit()
    conn.close()
    print("✅ bdl_data.db 파이프라인 GER/KST 정확한 타임존 날짜 반영 완료!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="BDL Pipeline Runner")
    parser.add_argument("--mode", choices=["predict", "score", "all"], default="all", help="Pipeline execution mode")
    args = parser.parse_args()

    print(f"🚀 Bundesliga (BDL) 정규 시즌 파이프라인 시작 (Mode: {args.mode})", flush=True)
    run_pipeline(mode=args.mode)
