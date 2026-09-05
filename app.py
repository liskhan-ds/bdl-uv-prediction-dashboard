import os
import sqlite3
import json
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
    "FC Cologne": "쾰른", "1. FC Köln": "쾰른", "Hamburg SV": "함부르크"
}

OFFICIAL_STATS = {
    "Harry Kane": (7.90, 0.90), "Florian Wirtz": (7.80, 0.45), "Jamal Musiala": (7.75, 0.40),
    "Serhou Guirassy": (7.65, 0.65), "Omar Marmoush": (7.65, 0.60), "Xavi Simons": (7.60, 0.35),
    "Joshua Kimmich": (7.60, 0.15), "Lois Openda": (7.55, 0.55), "Granit Xhaka": (7.55, 0.10),
    "Alejandro Grimaldo": (7.55, 0.25), "Jeremie Frimpong": (7.50, 0.22), "Victor Boniface": (7.50, 0.50),
    "Michael Olise": (7.50, 0.38), "Jonathan Tah": (7.45, 0.05), "Gregor Kobel": (7.45, 0.0),
    "Deniz Undav": (7.45, 0.48), "Alphonso Davies": (7.40, 0.08), "Nico Schlotterbeck": (7.40, 0.05),
    "Benjamin Sesko": (7.40, 0.45), "Manuel Neuer": (7.35, 0.0), "Leroy Sane": (7.35, 0.30),
    "Julian Brandt": (7.35, 0.25), "Kim Min-Jae": (7.35, 0.05), "Hugo Ekitike": (7.35, 0.35),
    "Andrej Kramaric": (7.35, 0.35), "Lukas Hradecky": (7.30, 0.0), "Dayot Upamecano": (7.30, 0.05),
    "Marcel Sabitzer": (7.30, 0.18), "Vincenzo Grifo": (7.30, 0.30), "Lee Jae-Sung": (7.25, 0.20),
    "Shuto Machino": (7.15, 0.30)
}

TEAM_GOALS_PER_GAME = {
    "바이에른 뮌헨": 2.60, "바이어 레버쿠젠": 2.40, "보루시아 도르트문트": 2.10, "RB 라이프치히": 2.00,
    "슈투트가르트": 1.90, "아인트라흐트 프랑크푸르트": 1.80, "호펜하임": 1.60, "프라이부르크": 1.50,
    "보루시아 묀헨글라트바흐": 1.45, "볼프스부르크": 1.40, "아우크스부르크": 1.30, "베르더 브레멘": 1.30,
    "마인츠 05": 1.25, "하이덴하임": 1.20, "우니온 베를린": 1.10, "홀슈타인 킬": 1.05,
    "장크트파울리": 1.00, "보훔": 0.95
}

TEAM_CONCEDED_PER_GAME = {
    "바이에른 뮌헨": 1.00, "바이어 레버쿠젠": 1.00, "RB 라이프치히": 1.10, "보루시아 도르트문트": 1.20,
    "아인트라흐트 프랑크푸르트": 1.30, "슈투트가르트": 1.30, "프라이부르크": 1.35, "우니온 베를린": 1.40,
    "장크트파울리": 1.45, "마인츠 05": 1.50, "볼프스부르크": 1.50, "베르더 브레멘": 1.55,
    "보루시아 묀헨글라트바흐": 1.55, "호펜하임": 1.60, "아우크스부르크": 1.60, "하이덴하임": 1.60,
    "홀슈타인 킬": 1.70, "보훔": 1.80
}

LOW_POSSESSION_TEAMS = ["우니온 베를린", "장크트파울리", "홀슈타인 킬", "보훔", "하이덴하임", "아우크스부르크"]

def normalize_team_name(raw_name):
    if not raw_name:
        return raw_name
    for key, val in TEAM_NAME_MAP.items():
        if key.lower() in raw_name.lower() or raw_name.lower() in key.lower():
            return val
    return raw_name

def calculate_player_uv(player_data, team_name=""):
    p_name_raw = player_data.get("name", "")
    rating = player_data.get("rating", None)
    goals_per90 = player_data.get("goals_per90", 0.0)
    position = player_data.get("pos", "M")
    
    for off_name, (off_r, off_g90) in OFFICIAL_STATS.items():
        if off_name.lower() in p_name_raw.lower() or p_name_raw.lower() in off_name.lower():
            if rating is None:
                rating = off_r
            goals_per90 = off_g90
            break
            
    pos_clean = "GK" if position in ["G", "GK"] else ("DF" if position in ["D", "DF"] else ("MF" if position in ["M", "MF"] else "FW"))
    
    tgoals = TEAM_GOALS_PER_GAME.get(team_name, 1.30)
    is_low_poss = team_name in LOW_POSSESSION_TEAMS
    
    if rating is None:
        if pos_clean == "GK": raw_uv = 0.95
        elif pos_clean == "DF": raw_uv = 0.90
        elif pos_clean == "MF": raw_uv = 0.82 if is_low_poss else 0.88
        else: raw_uv = 0.78 if tgoals < 1.1 else 0.85
    elif rating >= 6.65:
        if pos_clean == "GK": raw_uv = 1.0 + (rating - 6.65) * 0.45
        elif pos_clean == "DF": raw_uv = 1.0 + (rating - 6.65) * 0.40
        elif pos_clean == "MF":
            raw_uv = 1.0 + (rating - 6.65) * 0.35 - (0.08 if is_low_poss else 0.0)
        else: # FW
            raw_uv = 1.0 + (rating - 6.65) * 0.35 + (goals_per90 * 0.20)
            if goals_per90 < 0.15 or tgoals < 1.1:
                fw_penalty = min(0.15, round(0.10 + (0.15 - max(goals_per90, 0.0)) * 0.33, 3))
                raw_uv -= fw_penalty
    else:
        slope = 0.80 if pos_clean == "MF" else 0.65
        raw_uv = 1.0 + (rating - 6.65) * slope + (goals_per90 * 0.20 if pos_clean == "FW" else 0.0)
        if pos_clean == "MF" and is_low_poss: raw_uv -= 0.08
        elif pos_clean == "FW" and (goals_per90 < 0.15 or tgoals < 1.1):
            fw_penalty = min(0.15, round(0.10 + (0.15 - max(goals_per90, 0.0)) * 0.33, 3))
            raw_uv -= fw_penalty
        
    conc = TEAM_CONCEDED_PER_GAME.get(team_name, 1.30)
    if pos_clean in ["GK", "DF"] and conc > 1.4:
        def_penalty = min(0.12, round(0.04 + (conc - 1.4) * 0.10, 3))
        raw_uv -= def_penalty
        
    return round(min(max(raw_uv, 0.4), 2.0), 3)

def load_rosters():
    rosters_path = os.path.join(BASE_DIR, "rosters_2026.json")
    if os.path.exists(rosters_path):
        with open(rosters_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

ROSTERS_DATA = load_rosters()

def calculate_wuv_for_team(team_name, starters_override=None, subs_override=None):
    if starters_override is not None and subs_override is not None:
        starters = starters_override
        subs = subs_override
    else:
        norm_tname = normalize_team_name(team_name)
        plist = []
        for k, v in ROSTERS_DATA.items():
            if normalize_team_name(k) == norm_tname or k == norm_tname:
                plist = v
                break
        
        for p in plist:
            p["calc_uv"] = calculate_player_uv(p, team_name)
            
        gks = sorted([p for p in plist if p.get("pos") in ["G", "GK"]], key=lambda x: x["calc_uv"], reverse=True)
        dfs = sorted([p for p in plist if p.get("pos") in ["D", "DF"]], key=lambda x: x["calc_uv"], reverse=True)
        mfs = sorted([p for p in plist if p.get("pos") in ["M", "MF"]], key=lambda x: x["calc_uv"], reverse=True)
        fws = sorted([p for p in plist if p.get("pos") in ["F", "FW"]], key=lambda x: x["calc_uv"], reverse=True)
        
        starters = gks[:1] + dfs[:4] + mfs[:3] + fws[:3]
        subs = (gks[1:2] + dfs[4:6] + mfs[3:5] + fws[3:5])[:5]
        
    st_uvs = [calculate_player_uv(p, team_name) for p in starters]
    sub_uvs = [calculate_player_uv(p, team_name) for p in subs]
    
    st_avg = sum(st_uvs) / len(st_uvs) if st_uvs else 0.95
    sub_avg = sum(sub_uvs) / len(sub_uvs) if sub_uvs else 0.85
    
    raw_wuv = (0.85 * st_avg + 0.15 * sub_avg)
    team_wuv = round(11.0 + 10.5 * (raw_wuv - 0.835), 2)
    
    pos_sums = {"GK": 0.0, "DF": 0.0, "MF": 0.0, "FW": 0.0}
    for p in starters:
        uv = calculate_player_uv(p, team_name)
        pos = p.get("pos", "M")
        pos_clean = "GK" if pos in ["G","GK"] else ("DF" if pos in ["D","DF"] else ("MF" if pos in ["M","MF"] else "FW"))
        pos_sums[pos_clean] += uv
        
    st_tot_sum = sum(st_uvs)
    gk_wuv = round(team_wuv * (pos_sums["GK"] / st_tot_sum), 2) if st_tot_sum > 0 else 1.0
    df_wuv = round(team_wuv * (pos_sums["DF"] / st_tot_sum), 2) if st_tot_sum > 0 else 4.0
    mf_wuv = round(team_wuv * (pos_sums["MF"] / st_tot_sum), 2) if st_tot_sum > 0 else 3.0
    fw_wuv = round(team_wuv * (pos_sums["FW"] / st_tot_sum), 2) if st_tot_sum > 0 else 3.0
    
    return {
        "team_wuv": team_wuv,
        "st_avg": round(st_avg, 3),
        "sub_avg": round(sub_avg, 3),
        "gk_wuv": gk_wuv,
        "df_wuv": df_wuv,
        "mf_wuv": mf_wuv,
        "fw_wuv": fw_wuv
    }

def get_simulated_prediction(home_team, away_team, h_wuv, a_wuv):
    h_total = h_wuv + 0.25
    a_total = a_wuv
    gap = h_total - a_total
    
    if abs(gap) <= 0.40:
        winner = "무승부"
    elif gap > 0.40:
        winner = f"{home_team} 승"
    else:
        winner = f"{away_team} 승"
        
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
    
    if abs(gap) <= 0.40:
        sc_h = sc_a = int(round((sc_h + sc_a) / 2.0))
    elif gap > 0.40 and sc_h <= sc_a:
        sc_h = sc_a + 1
    elif gap < -0.40 and sc_a <= sc_h:
        sc_a = sc_h + 1
        
    return {
        "h_total": h_total, "a_total": a_total, "gap": gap, "winner": winner,
        "p_home": p_home, "p_draw": p_draw, "p_away": p_away, "sc_h": sc_h, "sc_a": sc_a
    }

def load_data():
    if not os.path.exists(DB_PATH):
        return pd.DataFrame([])
    try:
        conn = sqlite3.connect(DB_PATH)
        df_db = pd.read_sql_query("SELECT * FROM predictions ORDER BY id ASC", conn)
        conn.close()
        
        if not df_db.empty:
            if "round_name" not in df_db.columns:
                df_db["round_name"] = "Round 1 (Matchweek 1)"
            if "date" not in df_db.columns and "match_date" in df_db.columns:
                df_db["date"] = df_db["match_date"]
            if "uk_date" not in df_db.columns:
                df_db["uk_date"] = df_db["match_date"]
            if "kst_date" not in df_db.columns:
                df_db["kst_date"] = df_db["match_date"]
            if "visit_team" not in df_db.columns and "away_team" in df_db.columns:
                df_db["visit_team"] = df_db["away_team"]
            if "visit_uv" not in df_db.columns and "away_wuv" in df_db.columns:
                df_db["visit_uv"] = df_db["away_wuv"]
            if "home_uv" not in df_db.columns and "home_total_wuv" in df_db.columns:
                df_db["home_uv"] = df_db["home_total_wuv"]
            if "predicted_gap" not in df_db.columns and "gap" in df_db.columns:
                df_db["predicted_gap"] = df_db["gap"]
        return df_db
    except Exception as e:
        st.error(f"Error loading database: {e}")
        return pd.DataFrame([])

st.set_page_config(
    page_title="Bundesliga AI Predictor & WUV Dashboard",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Bundesliga (BDL) AI Match Predictor & Unit Value Dashboard")
st.markdown("독일 분데스리가 선수별 Unit Value(UV) 및 팀별 Weighted Unit Value(WUV) 기반 승패 예측 시스템")

df = load_data()

# -----------------------------------------------------------------------------
# Cumulative Metrics Header
# -----------------------------------------------------------------------------
st.header("📊 Cumulative Prediction Scorecard")

stats_df = df[df['actual_winner'].notna() & (df['actual_winner'] != '') & (~df['actual_winner'].isin(['Postponed', 'Canceled', '경기 연기', '경기 취소', '연기됨', '취소됨']))].copy() if not df.empty else pd.DataFrame()

col1, col2, col3, col4, col5 = st.columns(5)

if not stats_df.empty:
    tot_games = len(stats_df)
    corr_games = int(stats_df['is_correct'].sum())
    overall_acc = (corr_games / tot_games) * 100
    
    if overall_acc >= 55.0: tier = "🏆 God Tier"
    elif overall_acc >= 50.0: tier = "🥇 Master Tier (AI Default)"
    elif overall_acc >= 45.0: tier = "🥈 Pro Tier"
    elif overall_acc >= 38.0: tier = "🥉 Expert Tier"
    else: tier = "⚽ Amateur Tier"

    col1.metric("Overall Accuracy", f"{overall_acc:.2f}%", f"{tier}")
    col2.metric("Total Matchups Evaluated", f"{tot_games} Games")
    col3.metric("Correct Predictions", f"{corr_games} Wins")
    col4.metric("Pending Matches", f"{len(df) - tot_games} Games")
    col5.metric("System Status", "Live Predictions Active")
else:
    col1.metric("Overall Accuracy", "0.00%", "No Completed Matches")
    col2.metric("Total Matchups Evaluated", "0 Games")
    col3.metric("Correct Predictions", "0 Wins")
    col4.metric("Pending Matches", f"{len(df)} Games")
    col5.metric("System Status", "Live Predictions Active")

st.markdown("---")

# -----------------------------------------------------------------------------
# Prediction Scorecard by Round (Matchweek)
# -----------------------------------------------------------------------------
st.header("📈 Prediction Scorecard by Round (Bundesliga Matchweek)")

if not stats_df.empty:
    group_col = 'round_name' if 'round_name' in stats_df.columns else 'date'
    round_stats = stats_df.groupby(group_col, sort=False).agg(
        total_games=('home_team', 'count'),
        correct_games=('is_correct', 'sum')
    ).reset_index()

    round_stats['accuracy'] = (round_stats['correct_games'] / round_stats['total_games']) * 100
    
    def get_bar_color(acc):
        if acc >= 55: return '#A020F0'
        elif acc >= 50: return '#FF0000'
        elif acc >= 45: return '#FFA500'
        elif acc >= 38: return '#1E90FF'
        elif acc >= 30: return '#008000'
        else: return '#808080'

    round_stats['bar_color'] = round_stats['accuracy'].apply(get_bar_color)
    round_stats['label_text'] = round_stats.apply(
        lambda x: f"{int(x['correct_games'])}/{int(x['total_games'])}", 
        axis=1
    )

    round_stats_7d = round_stats.tail(10)

    base = alt.Chart(round_stats_7d).encode(x=alt.X(group_col, title='Bundesliga Matchweek', sort=None))
    bars = base.mark_bar().encode(
        y=alt.Y('accuracy', title='Accuracy (%)', scale=alt.Scale(domain=[0, 110])),
        color=alt.Color('bar_color', scale=None),
        tooltip=[group_col, 'accuracy', 'total_games', 'correct_games']
    )
    text = base.mark_text(align='center', baseline='bottom', dy=-5, fontSize=14, fontWeight='bold').encode(
        y='accuracy', text='label_text'
    )
    st.altair_chart((bars + text).properties(height=320), width='stretch')
else:
    st.info("💡 Scheduled match predictions complete! (Real-time accuracy by round will be tallied as matches complete.)")

st.markdown("""
<div style="text-align: center; padding: 12px; background-color: #f0f2f6; border-radius: 10px; line-height: 1.6;">
    <span style="color: #A020F0;">●</span> <b>God Tier</b> (55%↑) &nbsp;&nbsp;
    <span style="color: #FF0000;">●</span> <b>Master / AI</b> (50%~55%) &nbsp;&nbsp;
    <span style="color: #FFA500;">●</span> <b>Pro / Expert</b> (45%~50%) &nbsp;&nbsp;
    <span style="color: #1E90FF;">●</span> <b>Hardworking Amateur</b> (38%~45%) &nbsp;&nbsp;
    <span style="color: #008000;">●</span> <b>Normal Person</b> (30%~38%) &nbsp;&nbsp;
    <span style="color: #808080;">●</span> <b>Do Not Predict</b> (30%↓)
    <br><small>* Statistical breakeven is achieved from an average of ~46%-48%+ due to 3-Way (Win/Draw/Loss) nature.</small>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# Team WUV Leaderboard & Positional Breakdown
# -----------------------------------------------------------------------------
st.header("🛡️ Bundesliga Team Unit Value (WUV) Leaderboard")

bdl_teams = list(TEAM_GOALS_PER_GAME.keys())
unique_bdl_teams = sorted(list(set([normalize_team_name(t) for t in bdl_teams])))

wuv_list = []
for t in unique_bdl_teams:
    res = calculate_wuv_for_team(t)
    wuv_list.append({
        "Team": t,
        "Total WUV": res["team_wuv"],
        "GK WUV": res["gk_wuv"],
        "DF WUV": res["df_wuv"],
        "MF WUV": res["mf_wuv"],
        "FW WUV": res["fw_wuv"],
        "Starter Avg UV": res["st_avg"],
        "Sub Avg UV": res["sub_avg"]
    })

wuv_df = pd.DataFrame(wuv_list).sort_values(by="Total WUV", ascending=False).reset_index(drop=True)
wuv_df["Rank"] = range(1, len(wuv_df) + 1)

cols_wuv = ["Rank", "Team", "Total WUV", "GK WUV", "DF WUV", "MF WUV", "FW WUV", "Starter Avg UV", "Sub Avg UV"]
st.dataframe(wuv_df[cols_wuv], hide_index=True, width='stretch')

# Altair Team WUV Bar Chart
wuv_chart = alt.Chart(wuv_df).mark_bar(color='#E32219').encode(
    x=alt.X('Team', sort='-y', title='Team'),
    y=alt.Y('Total WUV', title='Weighted Unit Value (WUV)', scale=alt.Scale(domain=[7, 16])),
    tooltip=['Rank', 'Team', 'Total WUV', 'GK WUV', 'DF WUV', 'MF WUV', 'FW WUV']
).properties(height=350)
st.altair_chart(wuv_chart, width='stretch')

st.markdown("---")

# -----------------------------------------------------------------------------
# Gameweek Match Report Dataframe
# -----------------------------------------------------------------------------
st.header("📋 Bundesliga Gameweek Match Report")

def extract_round_num(text):
    import re
    m = re.search(r'Round\s*(\d+)', str(text))
    return int(m.group(1)) if m else 0

if not df.empty:
    if 'round_name' in df.columns:
        unique_dates = sorted(df['round_name'].unique(), key=extract_round_num)
        
        pending_df = df[df['actual_winner'].isna() | (df['actual_winner'] == '')]
        default_idx = 0
        if not pending_df.empty:
            pending_rounds = sorted(pending_df['round_name'].unique(), key=extract_round_num)
            target_round = pending_rounds[0]
            if target_round in unique_dates:
                default_idx = unique_dates.index(target_round)
                
        selected_date = st.selectbox("Select Matchweek to inspect:", unique_dates, index=default_idx)
        filtered_df = df[df['round_name'] == selected_date].copy().reset_index(drop=True)
    else:
        unique_dates = sorted(df['date'].unique())
        selected_date = st.selectbox("Select Matchweek to inspect:", unique_dates, index=0)
        filtered_df = df[df['date'] == selected_date].copy().reset_index(drop=True)

    if not filtered_df.empty:
        filtered_df['day_no'] = range(1, len(filtered_df) + 1)
        
        completed_in_round = filtered_df[filtered_df['actual_winner'].notna() & (filtered_df['actual_winner'] != '') & (~filtered_df['actual_winner'].isin(['Postponed', 'Canceled', '경기 연기', '경기 취소', '연기됨', '취소됨']))]
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Matches in Gameweek", f"{len(filtered_df)} Matches")
        col2.metric("Completed Matches", f"{len(completed_in_round)} Matches")
        
        if not completed_in_round.empty:
            corr_cnt = int(completed_in_round['is_correct'].sum())
            acc = (corr_cnt / len(completed_in_round)) * 100
            col3.metric("Gameweek Accuracy", f"{acc:.1f}% ({corr_cnt}/{len(completed_in_round)})")
        else:
            col3.metric("Gameweek Accuracy", "⏳ Scheduled")

        display_df = pd.DataFrame()
        display_df['No.'] = filtered_df['day_no']
        display_df['Match Date'] = filtered_df['match_date']
        display_df['Home Team'] = filtered_df.apply(lambda r: f"{r['home_team']} ({r['home_total_wuv']:.2f} WUV)" if ('home_total_wuv' in r and pd.notna(r.get('home_total_wuv'))) else f"{r['home_team']}", axis=1)
        display_df['Away Team'] = filtered_df.apply(lambda r: f"{r['visit_team']} ({r['away_total_wuv']:.2f} WUV)" if ('away_total_wuv' in r and pd.notna(r.get('away_total_wuv'))) else f"{r['visit_team']}", axis=1)
        display_df['AI Prediction'] = filtered_df['predicted_winner']
        display_df['3-Way Probabilities [Home%|Draw%|Away%]'] = filtered_df.apply(
            lambda r: f"[{r['prob_home']:.1f}% | {r['prob_draw']:.1f}% | {r['prob_away']:.1f}%]", axis=1
        )
        display_df['Predicted Gap (ΔWUV)'] = filtered_df['predicted_gap'].apply(lambda x: f"{x:+.2f}")
        display_df['Actual Result'] = filtered_df.apply(lambda r: f"{int(r['actual_score_home'])} : {int(r['actual_score_away'])} ({r['actual_winner']})" if (pd.notna(r.get('actual_score_home')) and pd.notna(r.get('actual_winner')) and r['actual_winner'] not in ['', 'Postponed', 'Canceled', '경기 연기', '경기 취소', '연기됨', '취소됨']) else (r['actual_winner'] if (pd.notna(r.get('actual_winner')) and r['actual_winner'] != '') else "Pending"), axis=1)
        
        def get_status_tag(r):
            act = r['actual_winner']
            if not act or pd.isna(act) or act == '':
                return "⏳ Pending"
            if act in ['Postponed', 'Canceled', '경기 연기', '경기 취소', '연기됨', '취소됨']:
                return "🚫 Postponed/Canceled"
            return "✅ Correct" if r['is_correct'] == 1 else "❌ Incorrect"
            
        display_df['Status'] = filtered_df.apply(get_status_tag, axis=1)

        st.dataframe(display_df, hide_index=True, width='stretch')

st.markdown("---")

# -----------------------------------------------------------------------------
# Interactive Match Simulator
# -----------------------------------------------------------------------------
st.header("⚡ Interactive Bundesliga Match Simulator")
st.markdown("선수 라인업 및 Unit Value 변경에 따른 실시간 WUV 및 승률 변화 시뮬레이션")

sim_col1, sim_col2 = st.columns(2)

with sim_col1:
    home_select = st.selectbox("Home Team Select:", unique_bdl_teams, index=0)
    home_wuv_info = calculate_wuv_for_team(home_select)
    st.metric(f"{home_select} Default WUV", f"{home_wuv_info['team_wuv']:.2f}")

with sim_col2:
    away_select = st.selectbox("Away Team Select:", unique_bdl_teams, index=1 if len(unique_bdl_teams)>1 else 0)
    away_wuv_info = calculate_wuv_for_team(away_select)
    st.metric(f"{away_select} Default WUV", f"{away_wuv_info['team_wuv']:.2f}")

sim_res = get_simulated_prediction(home_select, away_select, home_wuv_info['team_wuv'], away_wuv_info['team_wuv'])

st.subheader("🎯 Simulated Match Prediction Outcome")
res_c1, res_c2, res_c3, res_c4 = st.columns(4)
res_c1.metric("Predicted Winner", sim_res["winner"])
res_c2.metric("3-Way Odds", f"H {sim_res['p_home']}% | D {sim_res['p_draw']}% | A {sim_res['p_away']}%")
res_c3.metric("Predicted Score", f"{sim_res['sc_h']} : {sim_res['sc_a']}")
res_c4.metric("Adjusted Gap (ΔWUV)", f"{sim_res['gap']:+.2f}")

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #888888; padding-top: 20px;">
        <p>ⓒ DROPSHOT (사업자 번호: 578-81-03214)</p>
        <p>Contact us: liskhan@gmail.com</p>
    </div>
    """,
    unsafe_allow_html=True
)
