import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "bdl_data.db")

import json

TEAM_NAME_MAP = {
    "Manchester United": "맨체스터 유나이티드", "Arsenal": "아스널", "Manchester City": "맨체스터 시티",
    "Liverpool": "리버풀", "Chelsea": "첼시", "Tottenham Hotspur": "토트넘 홋스퍼", "Tottenham": "토트넘 홋스퍼",
    "Newcastle United": "뉴캐슬 유나이티드", "Newcastle": "뉴캐슬 유나이티드", "Aston Villa": "아스톤 빌라",
    "West Ham United": "웨스트햄 유나이티드", "West Ham": "웨스트햄 유나이티드", "Brighton & Hove Albion": "브라이튼",
    "Brighton": "브라이튼", "Fulham": "풀럼", "Crystal Palace": "크리스탈 팰리스", "Everton": "에버턴",
    "Wolverhampton Wanderers": "울버햄튼", "Wolves": "울버햄튼", "AFC Bournemouth": "본머스",
    "Bournemouth": "본머스", "Brentford": "브렌트포드", "Nottingham Forest": "노팅엄 포레스트",
    "Leicester City": "레스터 시티", "Ipswich Town": "입스위치 타운", "Southampton": "사우샘프턴",
    "Sunderland": "선덜랜드", "Burnley": "번리", "Leeds United": "리즈 유나이티드", "Leeds": "리즈 유나이티드",
    "Coventry City": "코번트리 시티", "Coventry": "코번트리 시티", "Hull City": "헐 시티", "Hull": "헐 시티"
}






def normalize_team_name(raw_name):
    for key, val in TEAM_NAME_MAP.items():
        if key.lower() in raw_name.lower() or raw_name.lower() in key.lower():
            return val
    return raw_name


OFFICIAL_STATS = {
    "Bukayo Saka": (7.75, 0.48), "Martin Ødegaard": (7.65, 0.35), "Declan Rice": (7.55, 0.20),
    "William Saliba": (7.50, 0.05), "Gabriel Magalhães": (7.45, 0.10), "Viktor Gyökeres": (7.70, 0.65),
    "Ben White": (7.30, 0.05), "David Raya": (7.25, 0.0), "Kai Havertz": (7.35, 0.38),
    "Gabriel Martinelli": (7.30, 0.30), "Leandro Trossard": (7.25, 0.32), "Kepa Arrizabalaga": (7.10, 0.0),
    "Erling Haaland": (7.85, 0.95), "Phil Foden": (7.65, 0.55), "Bernardo Silva": (7.45, 0.20),
    "Rúben Dias": (7.45, 0.05), "Josko Gvardiol": (7.40, 0.12), "Kevin De Bruyne": (7.75, 0.40),
    "Rodri": (7.60, 0.15), "Ederson": (7.25, 0.0), "Jérémy Doku": (7.30, 0.25), "Marc Guéhi": (7.35, 0.05),
    "Rayan Aït-Nouri": (7.25, 0.08), "Gerónimo Rulli": (7.15, 0.0),
    "Mohamed Salah": (7.80, 0.75), "Virgil van Dijk": (7.55, 0.08), "Trent Alexander-Arnold": (7.50, 0.12),
    "Florian Wirtz": (7.70, 0.45), "Alexis Mac Allister": (7.35, 0.18), "Dominik Szoboszlai": (7.30, 0.22),
    "Alisson Becker": (7.40, 0.0), "Luis Díaz": (7.35, 0.35), "Cody Gakpo": (7.25, 0.30),
    "Cole Palmer": (7.80, 0.60), "Moisés Caicedo": (7.40, 0.05), "Enzo Fernández": (7.30, 0.15),
    "Nicolas Jackson": (7.25, 0.40), "Pedro Neto": (7.20, 0.25), "Robert Sánchez": (7.15, 0.0),
    "Bruno Fernandes": (7.55, 0.30), "Marcus Rashford": (7.25, 0.32), "Alejandro Garnacho": (7.20, 0.28),
    "Kobbie Mainoo": (7.30, 0.15), "Matthijs de Ligt": (7.25, 0.08), "André Onana": (7.15, 0.0),
    "Son Heung-Min": (7.60, 0.50), "James Maddison": (7.30, 0.28), "Dominic Solanke": (7.20, 0.40),
    "Cristian Romero": (7.35, 0.10), "Micky van de Ven": (7.30, 0.08), "Guglielmo Vicario": (7.20, 0.0),
    "Ollie Watkins": (7.35, 0.45), "John McGinn": (7.15, 0.15), "Emiliano Martínez": (7.35, 0.0),
    "Alexander Isak": (7.45, 0.55), "Anthony Gordon": (7.25, 0.35), "Bruno Guimarães": (7.40, 0.15),
    "Kaoru Mitoma": (7.15, 0.25), "Evan Ferguson": (7.05, 0.30), "Bart Verbruggen": (7.10, 0.0),
    "Evanilson": (7.05, 0.35), "Justin Kluivert": (7.00, 0.25), "Fraser Forster": (7.00, 0.0),
    "Yoane Wissa": (7.05, 0.38), "Bryan Mbeumo": (7.30, 0.42), "Caoimhín Kelleher": (7.10, 0.0),
    "Jean-Philippe Mateta": (7.10, 0.42), "Eberechi Eze": (7.30, 0.30), "Dean Henderson": (7.10, 0.0),
    "Jordan Pickford": (7.20, 0.0), "Dwight McNeil": (6.95, 0.15), "Jarrad Branthwaite": (7.20, 0.05),
    "Bernd Leno": (7.15, 0.0), "Alex Iwobi": (7.00, 0.18), "Emile Smith Rowe": (7.10, 0.22),
    "Chris Wood": (6.75, 0.32), "Morgan Gibbs-White": (7.15, 0.20), "Matz Sels": (7.00, 0.0),
    "Liam Delap": (6.45, 0.10), "Arijanet Muric": (6.50, 0.0),
    "Illan Meslier": (6.40, 0.0), "Daniel James": (6.45, 0.12),
    "Haji Wright": (6.40, 0.10), "Oliver Dovin": (6.45, 0.0),
    "Oscar Estupiñan": (6.35, 0.08), "Ivor Pandur": (6.40, 0.0),
    "Wilson Isidor": (6.35, 0.08), "Anthony Patterson": (6.40, 0.0),
}

TEAM_CONCEDED_PER_GAME = {
    "Arsenal": 0.8, "Manchester City": 0.9, "Liverpool": 1.0, "Chelsea": 1.2,
    "Manchester United": 1.3, "Tottenham Hotspur": 1.35, "Aston Villa": 1.3,
    "Newcastle United": 1.35, "Brighton & Hove Albion": 1.4, "AFC Bournemouth": 1.45,
    "Brentford": 1.50, "Crystal Palace": 1.50, "Fulham": 1.55, "Everton": 1.60,
    "Nottingham Forest": 1.65, "Ipswich Town": 1.75, "Leeds United": 1.80,
    "Coventry City": 1.85, "Sunderland": 1.90, "Hull City": 1.95,
}

TEAM_GOALS_PER_GAME = {
    "Arsenal": 2.2, "Manchester City": 2.3, "Liverpool": 2.1, "Chelsea": 1.8,
    "Manchester United": 1.6, "Tottenham Hotspur": 1.7, "Aston Villa": 1.6,
    "Newcastle United": 1.5, "Brighton & Hove Albion": 1.4, "AFC Bournemouth": 1.3,
    "Brentford": 1.2, "Crystal Palace": 1.1, "Fulham": 1.15, "Everton": 1.0,
    "Nottingham Forest": 1.05, "Ipswich Town": 0.95, "Leeds United": 0.90,
    "Coventry City": 0.85, "Sunderland": 0.80, "Hull City": 0.75,
}

LOW_POSSESSION_TEAMS = ["Everton", "Nottingham Forest", "Ipswich Town", "Leeds United", "Coventry City", "Sunderland", "Hull City"]

MATCHWEEK_1_ABSENCES = {
    "Arsenal": ["William Saliba", "Jurriën Timber"],
    "Chelsea": ["Wesley Fofana"],
    "Fulham": ["Joachim Andersen"],
    "Manchester United": ["Rasmus Højlund", "Tyrell Malacia"],
    "Tottenham Hotspur": ["Richarlison"],
    "Liverpool": ["Stefan Bajcetic"],
    "Newcastle United": ["Sven Botman"],
    "Aston Villa": ["Boubacar Kamara"],
}

def get_team_roster(team_name, absentees=None):
    if not os.path.exists("rosters_2026.json"):
        return {"starters": [], "subs": []}
    with open("rosters_2026.json", "r", encoding="utf-8") as f:
        rosters = json.load(f)
        
    normalized_map = {normalize_team_name(k): v for k, v in rosters.items()}
    norm_tname = normalize_team_name(team_name)
    plist = normalized_map.get(norm_tname, [])
    
    if absentees is None:
        absentees = MATCHWEEK_1_ABSENCES.get(team_name, [])
        
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
    p_name = normalize_team_name(p_name_raw) if "normalize_team_name" in globals() else p_name_raw.strip()
    
    rating = None
    goals_per90 = 0.0
    position = player_data.get("pos", "M")
    
    matched = False
    for off_name, (off_r, off_g90) in OFFICIAL_STATS.items():
        if off_name.lower() in p_name_raw.lower() or p_name_raw.lower() in off_name.lower():
            rating = off_r
            goals_per90 = off_g90
            matched = True
            break
            
    if not matched and os.path.exists(DB_PATH):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT rating, goals_per90, position FROM player_stats WHERE player_name = ? OR player_name LIKE ?", (p_name_raw, f"%{p_name_raw}%"))
            row = cursor.fetchone()
            if row:
                rating = row[0]
                goals_per90 = row[1]
                position = row[2]
            conn.close()
        except Exception:
            pass
            
    pos_clean = "GK" if position in ["G", "GK"] else ("DF" if position in ["D", "DF"] else ("MF" if position in ["M", "MF"] else "FW"))
    
    tgoals = TEAM_GOALS_PER_GAME.get(team_name, 1.30)
    is_low_poss = team_name in LOW_POSSESSION_TEAMS
    
    if rating is None:
        if pos_clean == "GK":
            raw_uv = 0.95
        elif pos_clean == "DF":
            raw_uv = 0.90
        elif pos_clean == "MF":
            raw_uv = 0.82 if is_low_poss else 0.88
        else: # FW
            raw_uv = 0.78 if tgoals < 1.1 else 0.85
    elif rating >= 6.65:
        if pos_clean == "GK":
            raw_uv = 1.0 + (rating - 6.65) * 0.45
        elif pos_clean == "DF":
            raw_uv = 1.0 + (rating - 6.65) * 0.40
        elif pos_clean == "MF":
            raw_uv = 1.0 + (rating - 6.65) * 0.35
            if is_low_poss:
                raw_uv -= 0.08
        else: # FW
            raw_uv = 1.0 + (rating - 6.65) * 0.35 + (goals_per90 * 0.20)
            if goals_per90 < 0.15 or tgoals < 1.1:
                fw_penalty = min(0.15, round(0.10 + (0.15 - max(goals_per90, 0.0)) * 0.33, 3))
                raw_uv -= fw_penalty
    else:
        # rating < 6.65 penalty: MF slope 0.80
        slope = 0.80 if pos_clean == "MF" else 0.65
        raw_uv = 1.0 + (rating - 6.65) * slope + (goals_per90 * 0.20 if pos_clean == "FW" else 0.0)
        if pos_clean == "MF" and is_low_poss:
            raw_uv -= 0.08
        elif pos_clean == "FW" and (goals_per90 < 0.15 or tgoals < 1.1):
            fw_penalty = min(0.15, round(0.10 + (0.15 - max(goals_per90, 0.0)) * 0.33, 3))
            raw_uv -= fw_penalty
        
    # Defense/GK conceded penalty if team conceded > 1.4 per game
    conc = TEAM_CONCEDED_PER_GAME.get(team_name, 1.30)
    if pos_clean in ["GK", "DF"] and conc > 1.4:
        def_penalty = min(0.12, round(0.04 + (conc - 1.4) * 0.10, 3))
        raw_uv -= def_penalty
        
    return round(min(max(raw_uv, 0.4), 2.0), 3)

def calculate_wuv(team_name, absentees=None):
    roster = get_team_roster(team_name, absentees=absentees)
    starters = roster.get("starters", [])
    subs = roster.get("subs", [])
    
    st_uvs = [calculate_player_uv(p, team_name) for p in starters]
    sub_uvs = [calculate_player_uv(p, team_name) for p in subs]
    
    st_avg = sum(st_uvs) / len(st_uvs) if st_uvs else 0.95
    sub_avg = sum(sub_uvs) / len(sub_uvs) if sub_uvs else 0.85
    
    raw_wuv = (0.85 * st_avg + 0.15 * sub_avg)
    team_wuv = round(11.0 + 10.5 * (raw_wuv - 0.835), 2)
    
    # Position detail breakdown
    pos_sums = {"GK": 0.0, "DF": 0.0, "MF": 0.0, "FW": 0.0}
    starters_detail = []
    for p in starters:
        uv = calculate_player_uv(p, team_name)
        pos = p.get("pos", "M")
        pos_clean = "GK" if pos in ["G","GK"] else ("DF" if pos in ["D","DF"] else ("MF" if pos in ["M","MF"] else "FW"))
        pos_sums[pos_clean] += uv
        starters_detail.append({"name": p.get("name"), "pos": pos_clean, "uv": uv})
        
    st_tot_sum = sum(st_uvs)
    gk_wuv = round(team_wuv * (pos_sums["GK"] / st_tot_sum), 2) if st_tot_sum > 0 else 1.0
    df_wuv = round(team_wuv * (pos_sums["DF"] / st_tot_sum), 2) if st_tot_sum > 0 else 4.0
    mf_wuv = round(team_wuv * (pos_sums["MF"] / st_tot_sum), 2) if st_tot_sum > 0 else 3.0
    fw_wuv = round(team_wuv * (pos_sums["FW"] / st_tot_sum), 2) if st_tot_sum > 0 else 3.0
    
    return {
        "team_wuv": team_wuv,
        "st_avg": round(st_avg, 3),
        "sub_avg": round(sub_avg, 3),
        "st_sum": round(st_tot_sum, 3),
        "sub_sum": round(sum(sub_uvs), 3),
        "gk_wuv": gk_wuv,
        "df_wuv": df_wuv,
        "mf_wuv": mf_wuv,
        "fw_wuv": fw_wuv,
        "starters_detail": starters_detail
    }

import json
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.graph_objects as go
import sqlite3
import os
from datetime import datetime

# -----------------------------------------------------------------------------
# 1. Page Configuration and Unified Top Navigation
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="BDL AI Match Predictor",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Top Navigation Bar (7 Leagues)
nav_cols = st.columns(7)
with nav_cols[0]:
    st.link_button("🏀 NBA ↗", "https://nba-uv-prediction.streamlit.app/", use_container_width=True)
with nav_cols[1]:
    st.link_button("⚾ MLB ↗", "https://mlb-uv-prediction.streamlit.app/", use_container_width=True)
with nav_cols[2]:
    st.button("⚽ EPL (Current)", disabled=True, use_container_width=True)
with nav_cols[3]:
    st.link_button("⚽ La Liga ↗", "https://llg-uv-prediction.streamlit.app/", use_container_width=True)
with nav_cols[4]:
    st.link_button("🏒 NHL ↗", "https://nhl-uv-prediction.streamlit.app/", use_container_width=True)
with nav_cols[5]:
    st.link_button("🏈 NFL ↗", "https://nfl-uv-prediction.streamlit.app/", use_container_width=True)
with nav_cols[6]:
    st.link_button("⚽ MLS ↗", "https://mls-uv-prediction.streamlit.app/", use_container_width=True)

st.divider()

# Main Title and Description
st.title("⚽ BDL AI Match Predictor")

# -----------------------------------------------------------------------------
# 2. EPL Team Roster UV Database (20 Clubs, 11 Starters + 5 Subs)
# -----------------------------------------------------------------------------
TEAMS_ROSTER = {
    "본머스": {
        "starters": [
            {
                "pos": "GK",
                "name": "Fraser Forster",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Adam Smith",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Max Aarons",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "James Hill",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Julián Araujo",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "David Brooks",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Ryan Christie",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Tyler Adams",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Evanilson",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Justin Kluivert",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Amine Adli",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Michele Di Gregorio",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Bafodé Diakité",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Adrien Truffert",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Lewis Cook",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Marcus Tavernier",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "아스널": {
        "starters": [
            {
                "pos": "GK",
                "name": "케파 아리사발라가",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Ezri Konsa",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "가브리엘 마갈량이스",
                "att_uv": 0.45,
                "def_uv": 0.65
            },
            {
                "pos": "DF",
                "name": "벤 화이트",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "윌리엄 살리바",
                "att_uv": 0.45,
                "def_uv": 0.7
            },
            {
                "pos": "MF",
                "name": "Fabio Vieira",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "마르틴 외데고르",
                "att_uv": 0.8,
                "def_uv": 0.35
            },
            {
                "pos": "MF",
                "name": "미켈 메리노",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "가브리엘 제수스",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "카이 하베르츠",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "빅토르 예케레스",
                "att_uv": 0.85,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "다비드 라야",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "율리엔 팀버",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Piero Hincapié",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "브루노 기마랑이스",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "데클런 라이스",
                "att_uv": 0.55,
                "def_uv": 0.6
            }
        ]
    },
    "아스톤 빌라": {
        "starters": [
            {
                "pos": "GK",
                "name": "Marco Bizot",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Tyrone Mings",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Victor Lindelöf",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Matty Cash",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Aaron Wan-Bissaka",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Ross Barkley",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "John McGinn",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Leon Goretzka",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Ollie Watkins",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Leon Bailey",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Tammy Abraham",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Emiliano Martínez",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Pau Torres",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Ian Maatsen",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Emiliano Buendía",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Boubacar Kamara",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "브렌트포드": {
        "starters": [
            {
                "pos": "GK",
                "name": "Ellery Balcombe",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Kristoffer Ajer",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Rico Henry",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Sepp van den Berg",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Nathan Collins",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Vitaly Janelt",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Mathias Jensen",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Mamadou Sangare",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Callum Wilson",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Keane Lewis-Potter",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Igor Thiago",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Caoimhín Kelleher",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Aaron Hickey",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Jayden Meghoma",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Fábio Carvalho",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Josh Dasilva",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "브라이튼": {
        "starters": [
            {
                "pos": "GK",
                "name": "Jason Steele",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Lewis Dunk",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Olivier Boscagli",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Igor Julio",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Ferdi Kadioglu",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Pascal Gross",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Diego Gómez",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Matt O'Riley",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Georginio Rutter",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Evan Ferguson",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Promise David",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Tom McGill",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Pascal Struijk",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Costinha",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Kaoru Mitoma",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Mats Wieffer",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "첼시": {
        "starters": [
            {
                "pos": "GK",
                "name": "로베르트 산체스",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "리스 제임스",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Tosin Adarabioyo",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Maxence Lacroix",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "웨슬리 포파나",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Jordan Henderson",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Morgan Rogers",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "엔초 페르난데스",
                "att_uv": 0.6,
                "def_uv": 0.5
            },
            {
                "pos": "FW",
                "name": "Danny Welbeck",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "페드로 네투",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "주앙 페드로",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Gaga Slonina",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "리바이 콜윌",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Pep Chavarría",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "모이세스 카이세도",
                "att_uv": 0.5,
                "def_uv": 0.6
            },
            {
                "pos": "MF",
                "name": "콜 파머",
                "att_uv": 0.9,
                "def_uv": 0.3
            }
        ]
    },
    "코번트리 시티": {
        "starters": [
            {
                "pos": "GK",
                "name": "Daniel Bentley",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Jake Bidwell",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Jay Da Silva",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Ethan Pinnock",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Joel Latibeaudiere",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Matt Grimes",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Gustavo Hamer",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Ephron Mason-Clark",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "FW",
                "name": "Taiwo Awoniyi",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Haji Wright",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Brandon Thomas-Asante",
                "att_uv": 0.66,
                "def_uv": 0.24
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Ben Wilson",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Luke Woolfenden",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Liam Kitching",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Victor Torp",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Frank Onyeka",
                "att_uv": 0.48,
                "def_uv": 0.42
            }
        ]
    },
    "크리스탈 팰리스": {
        "starters": [
            {
                "pos": "GK",
                "name": "Walter Benítez",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Daniel Muñoz",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Borna Sosa",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Axel Disasi",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Takehiro Tomiyasu",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Will Hughes",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Jefferson Lerma",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Daichi Kamada",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Ismaïla Sarr",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Jean-Philippe Mateta",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Jørgen Strand Larsen",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Remi Matthews",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Chris Richards",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Óscar Mingueza",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Cheick Doucouré",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Justin Devenny",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "에버턴": {
        "starters": [
            {
                "pos": "GK",
                "name": "Mark Travers",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Michael Keane",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "James Tarkowski",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Vitaliy Mykolenko",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Nathan Patterson",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Christian Nørgaard",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Kiernan Dewsbury-Hall",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "James Garner",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Iliman Ndiaye",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Beto",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Brennan Johnson",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Tom King",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Jake O'Brien",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Jarrad Branthwaite",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Hayden Hackney",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Charly Alcaraz",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "풀럼": {
        "starters": [
            {
                "pos": "GK",
                "name": "Benjamin Lecomte",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Kenny Tete",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Joachim Andersen",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Timothy Castagne",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Antonee Robinson",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "César Palacios",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Tom Cairney",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Harrison Reed",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Gonzalo García",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Alex Iwobi",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Rodrigo Muniz",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Bernd Leno",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Jorge Cuenca",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Calvin Bassey",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Sander Berge",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Ryan Sessegnon",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "헐 시티": {
        "starters": [
            {
                "pos": "GK",
                "name": "Jack Butland",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "John Egan",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Semi Ajayi",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Matt Targett",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Paddy McNair",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Matt Crooks",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Kieran Dowell",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Abdülkadir Ömür",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "FW",
                "name": "Oliver McBurnie",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Babajide David",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Liam Millar",
                "att_uv": 0.66,
                "def_uv": 0.24
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Dillon Phillips",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Lewie Coyle",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Ryan Giles",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Regan Slater",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Hidemasa Morita",
                "att_uv": 0.48,
                "def_uv": 0.42
            }
        ]
    },
    "입스위치 타운": {
        "starters": [
            {
                "pos": "GK",
                "name": "David Button",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Darnell Furlong",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Issa Diop",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Dara O'Shea",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Cedric Kipre",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Julio Enciso",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Jack Taylor",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Cameron Humphreys",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "FW",
                "name": "Chuba Akpom",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Chiedozie Ogbene",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Jack Clarke",
                "att_uv": 0.66,
                "def_uv": 0.24
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Christian Walton",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Leif Davis",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Jacob Greaves",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Sasa Lukic",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Exequiel Palacios",
                "att_uv": 0.48,
                "def_uv": 0.42
            }
        ]
    },
    "리즈 유나이티드": {
        "starters": [
            {
                "pos": "GK",
                "name": "Alex Cairns",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Nico Elvedi",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "James Justin",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Joe Rodon",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Jayden Bogle",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Ilia Gruev",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Ethan Ampadu",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Sean Longstaff",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "FW",
                "name": "Harry Wilson",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Dominic Calvert-Lewin",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Daniel James",
                "att_uv": 0.66,
                "def_uv": 0.24
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Lucas Perri",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Gabriel Gudmundsson",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Jaka Bijol",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Ao Tanaka",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Brenden Aaronson",
                "att_uv": 0.48,
                "def_uv": 0.42
            }
        ]
    },
    "리버풀": {
        "starters": [
            {
                "pos": "GK",
                "name": "알리송 베케르",
                "att_uv": 0.3,
                "def_uv": 0.65
            },
            {
                "pos": "DF",
                "name": "조 고메스",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "버질 반 다이크",
                "att_uv": 0.45,
                "def_uv": 0.7
            },
            {
                "pos": "DF",
                "name": "Kostas Tsimikas",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Conor Bradley",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Wataru Endo",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "알렉시스 맥 알리스터",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "도미니크 소보슬라이",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "페데리코 키에사",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "알렉산데르 이삭",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "코디 각포",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Freddie Woodman",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "로날드 아라우호",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "제레미 프림퐁",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "라이언 흐라번베르흐",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Harvey Elliott",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "맨체스터 시티": {
        "starters": [
            {
                "pos": "GK",
                "name": "헤로니모 룰리",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "후벵 디아스",
                "att_uv": 0.45,
                "def_uv": 0.65
            },
            {
                "pos": "DF",
                "name": "마크 게히",
                "att_uv": 0.4,
                "def_uv": 0.65
            },
            {
                "pos": "DF",
                "name": "라얀 아이트-누리",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "요슈코 그바르디올",
                "att_uv": 0.5,
                "def_uv": 0.6
            },
            {
                "pos": "MF",
                "name": "마테오 코바치치",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "잭 그릴리시",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Elliot Anderson",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "엘링 홀란드",
                "att_uv": 0.9,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "앙투안 세메뇨",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "제레미 도쿠",
                "att_uv": 0.75,
                "def_uv": 0.3
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Marcus Bettinelli",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Josh Wilson-Esbrand",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "리코 루이스",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "필 포든",
                "att_uv": 0.8,
                "def_uv": 0.35
            },
            {
                "pos": "MF",
                "name": "라얀 체르키",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "맨체스터 유나이티드": {
        "starters": [
            {
                "pos": "GK",
                "name": "Tom Heaton",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "해리 매과이어",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "루크 쇼",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "리산드로 마르티네스",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "디오구 달롯",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "브루노 페르난데스",
                "att_uv": 0.75,
                "def_uv": 0.4
            },
            {
                "pos": "MF",
                "name": "유리 틸레만스",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Jack Fletcher",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "마커스 래시포드",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "마테우스 쿠냐",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "브라이언 음베우모",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "칼 다를로우",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "마테이스 더 리흐트",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "누사이르 마즈라위",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "메이슨 마운트",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "마누엘 우가르테",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "뉴캐슬 유나이티드": {
        "starters": [
            {
                "pos": "GK",
                "name": "Mark Gillespie",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Lewis Hall",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Fabian Schär",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Dan Burn",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Sven Botman",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Jacob Murphy",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Joelinton",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Harvey Barnes",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "Yoane Wissa",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Anthony Elanga",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "Nick Woltemade",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Nick Pope",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "Tino Livramento",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Malick Thiaw",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "Joe Willock",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "Jacob Ramsey",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    },
    "노팅엄 포레스트": {
        "starters": [
            {
                "pos": "GK",
                "name": "Matz Sels",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Morato",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Ola Aina",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Nikola Milenkovic",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Neco Williams",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Ibrahim Sangaré",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Xaver Schlager",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Ryan Yates",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "FW",
                "name": "Chris Wood",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Callum Hudson-Odoi",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Dan Ndoye",
                "att_uv": 0.66,
                "def_uv": 0.24
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "John Victor",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Luca Netz",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Jair Paula",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Morgan Gibbs-White",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Nicolás Domínguez",
                "att_uv": 0.48,
                "def_uv": 0.42
            }
        ]
    },
    "선덜랜드": {
        "starters": [
            {
                "pos": "GK",
                "name": "Simon Moore",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Thomas Meunier",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Nordi Mukiele",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Omar Alderete",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Reinildo Mandava",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Abdoullah Ba",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Granit Xhaka",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Luke O'Nien",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "FW",
                "name": "Wilson Isidor",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Brian Brobbey",
                "att_uv": 0.66,
                "def_uv": 0.24
            },
            {
                "pos": "FW",
                "name": "Simon Adingra",
                "att_uv": 0.66,
                "def_uv": 0.24
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Robin Roefs",
                "att_uv": 0.2,
                "def_uv": 0.55
            },
            {
                "pos": "DF",
                "name": "Ajibola Alese",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "DF",
                "name": "Danny Ballard",
                "att_uv": 0.4,
                "def_uv": 0.5
            },
            {
                "pos": "MF",
                "name": "Alan Browne",
                "att_uv": 0.48,
                "def_uv": 0.42
            },
            {
                "pos": "MF",
                "name": "Enzo Le Fée",
                "att_uv": 0.48,
                "def_uv": 0.42
            }
        ]
    },
    "토트넘 홋스퍼": {
        "starters": [
            {
                "pos": "GK",
                "name": "마르틴 두브라브카",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "벤 데이비스",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "앤디 로버트슨",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "마르코스 세네시",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Kevin Danso",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "제임스 매디슨",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "로드리고 벤탕쿠르",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "산드로 토날리",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "FW",
                "name": "히샤를리송",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "도미닉 솔랑케",
                "att_uv": 0.73,
                "def_uv": 0.25
            },
            {
                "pos": "FW",
                "name": "오마르 마르무시",
                "att_uv": 0.73,
                "def_uv": 0.25
            }
        ],
        "subs": [
            {
                "pos": "GK",
                "name": "Brandon Austin",
                "att_uv": 0.25,
                "def_uv": 0.6
            },
            {
                "pos": "DF",
                "name": "페드로 포로",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "DF",
                "name": "Jan Paul van Hecke",
                "att_uv": 0.44,
                "def_uv": 0.54
            },
            {
                "pos": "MF",
                "name": "모하메드 쿠두스",
                "att_uv": 0.54,
                "def_uv": 0.44
            },
            {
                "pos": "MF",
                "name": "코너 갤러거",
                "att_uv": 0.54,
                "def_uv": 0.44
            }
        ]
    }
}

def ensure_team_roster(team_name):
    if team_name not in TEAMS_ROSTER:
        TEAMS_ROSTER[team_name] = {
            "starters": [
                {"pos": "GK", "name": f"{team_name} GK", "att_uv": 0.15, "def_uv": 0.45},
                {"pos": "DF", "name": f"{team_name} DF1", "att_uv": 0.30, "def_uv": 0.45},
                {"pos": "DF", "name": f"{team_name} DF2", "att_uv": 0.25, "def_uv": 0.50},
                {"pos": "DF", "name": f"{team_name} DF3", "att_uv": 0.25, "def_uv": 0.50},
                {"pos": "DF", "name": f"{team_name} DF4", "att_uv": 0.35, "def_uv": 0.40},
                {"pos": "MF", "name": f"{team_name} MF1", "att_uv": 0.40, "def_uv": 0.45},
                {"pos": "MF", "name": f"{team_name} MF2", "att_uv": 0.40, "def_uv": 0.45},
                {"pos": "MF", "name": f"{team_name} MF3", "att_uv": 0.55, "def_uv": 0.35},
                {"pos": "FW", "name": f"{team_name} FW1", "att_uv": 0.60, "def_uv": 0.25},
                {"pos": "FW", "name": f"{team_name} FW2", "att_uv": 0.60, "def_uv": 0.25},
                {"pos": "FW", "name": f"{team_name} FW3", "att_uv": 0.65, "def_uv": 0.20},
            ],
            "subs": [
                {"pos": "FW", "name": f"{team_name} Sub1", "att_uv": 0.50, "def_uv": 0.20},
                {"pos": "MF", "name": f"{team_name} Sub2", "att_uv": 0.40, "def_uv": 0.30},
                {"pos": "MF", "name": f"{team_name} Sub3", "att_uv": 0.35, "def_uv": 0.35},
                {"pos": "DF", "name": f"{team_name} Sub4", "att_uv": 0.20, "def_uv": 0.40},
                {"pos": "GK", "name": f"{team_name} Sub5", "att_uv": 0.10, "def_uv": 0.35},
            ]
        }




def get_match_prediction(home_team, away_team):
    h_info = calculate_wuv(home_team)
    a_info = calculate_wuv(away_team)
    
    h_total = h_info["team_wuv"] + 0.25
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
    
    # Ensure score consistency with winner prediction
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




def load_data():
    if not os.path.exists(DB_PATH):
        return pd.DataFrame([])
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(predictions)")
        cols = [row[1] for row in cursor.fetchall()]
        
        order_col = "date" if "date" in cols else "id"
        df_db = pd.read_sql_query(f"SELECT * FROM predictions ORDER BY {order_col} ASC", conn)
        conn.close()
        
        if not df_db.empty:
            if "round_name" not in df_db.columns:
                df_db["round_name"] = "Round 1 (Gameweek 1)"
            if "date" not in df_db.columns and "match_date" in df_db.columns:
                df_db["date"] = df_db["match_date"]
            if "uk_date" not in df_db.columns:
                df_db["uk_date"] = df_db.get("date", df_db.get("match_date", "2026-08"))
            if "kst_date" not in df_db.columns:
                df_db["kst_date"] = df_db.get("date", df_db.get("match_date", "2026-08"))
            if "visit_team" not in df_db.columns and "away_team" in df_db.columns:
                df_db["visit_team"] = df_db["away_team"]
            if "visit_uv" not in df_db.columns and "away_wuv" in df_db.columns:
                df_db["visit_uv"] = df_db["away_wuv"]
            if "home_uv" not in df_db.columns and "home_total_wuv" in df_db.columns:
                df_db["home_uv"] = df_db["home_total_wuv"]
            if "predicted_gap" not in df_db.columns and "gap" in df_db.columns:
                df_db["predicted_gap"] = df_db["gap"]
            if "actual_winner" not in df_db.columns:
                df_db["actual_winner"] = ""
            if "is_correct" not in df_db.columns:
                df_db["is_correct"] = None
                
        return df_db
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame([])


df = load_data()

if not df.empty and "actual_winner" in df.columns:
    df["total_no"] = range(1, len(df) + 1)
    stats_df = df[df["actual_winner"].notna() & (df["actual_winner"] != "")].copy()
else:
    df = pd.DataFrame(columns=[
        "total_no", "date", "uk_date", "kst_date", "round_name", "home_team", "visit_team",
        "predicted_winner", "predicted_gap", "prob_home", "prob_draw", "prob_away",
        "home_uv", "visit_uv", "actual_winner", "actual_score_home", "actual_score_away", "is_correct"
    ])
    stats_df = pd.DataFrame([])

st.header("📊 Cumulative Prediction Scorecard")
total_stats = len(stats_df)
correct_total = stats_df['is_correct'].sum() if total_stats > 0 else 0

col_acc, col_track = st.columns([2, 1])

if total_stats > 0:
    total_acc = (correct_total / total_stats) * 100
    status_suffix = " (⚡ God Tier, Market Distortion)" if total_acc >= 55 else ""
    
    with col_acc:
        st.subheader(f"Overall Completed Match Accuracy: `{total_acc:.2f}%`{status_suffix}")
        st.markdown(f"**Correct Predictions:** {int(correct_total)} / **Completed Matches:** {total_stats} (Total Scheduled: {len(df)} Games)")
    
    with col_track:
        remaining = 100 - total_stats
        if remaining > 0:
            st.metric("Matches Until 100-Game System Validation", f"{remaining} Games Remaining")
        else:
            st.metric("System Validation Status", "Validation Complete (God Tier)")
else:
    with col_acc:
        st.subheader(f"Total Target Matches: `{len(df)} Games`")
        st.markdown(f"**Predicted Matches:** {len(df)} Games (Live Accuracy Tallying)")
    with col_track:
        st.metric("System Status", "Live Predictions Active")

st.markdown("---")

# -----------------------------------------------------------------------------
# 6. Prediction Scorecard by Round (BDL Gameweek)
# -----------------------------------------------------------------------------
st.header("📈 Prediction Scorecard by Round (BDL Gameweek)")

if not stats_df.empty:
    group_col = 'round_name' if 'round_name' in stats_df.columns else 'date'
    round_stats = stats_df.groupby(group_col, sort=False).agg(
        total_games=('home_team', 'count'),
        correct_games=('is_correct', 'sum')
    ).reset_index()

    round_stats['accuracy'] = (round_stats['correct_games'] / round_stats['total_games']) * 100
    
    def get_bar_color(acc):
        if acc >= 55: return '#A020F0'      # Purple (God Tier)
        elif acc >= 50: return '#FF0000'    # Red (Master / AI)
        elif acc >= 45: return '#FFA500'    # Orange (Pro / Expert)
        elif acc >= 38: return '#1E90FF'    # Blue (Hardworking Amateur)
        elif acc >= 30: return '#008000'    # Green (Normal Person)
        else: return '#808080'             # Gray (Do Not Predict)

    round_stats['bar_color'] = round_stats['accuracy'].apply(get_bar_color)
    round_stats['label_text'] = round_stats.apply(
        lambda x: f"{int(x['correct_games'])}/{int(x['total_games'])}", 
        axis=1
    )

    round_stats_7d = round_stats.tail(7)

    base = alt.Chart(round_stats_7d).encode(x=alt.X(group_col, title='BDL Gameweek', sort=None))
    bars = base.mark_bar().encode(
        y=alt.Y('accuracy', title='Accuracy (%)', scale=alt.Scale(domain=[0, 110])),
        color=alt.Color('bar_color', scale=None),
        tooltip=[group_col, 'accuracy', 'total_games', 'correct_games']
    )
    text = base.mark_text(align='center', baseline='bottom', dy=-5, fontSize=14, fontWeight='bold').encode(
        y='accuracy', text='label_text'
    )
    st.altair_chart((bars + text).properties(height=320), use_container_width=True)
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
# 7. Gameweek Match Report (Matchup Card List)
# -----------------------------------------------------------------------------
st.header("📋 Gameweek Match Report (10 Matchups)")

def extract_round_num(text):
    import re
    m = re.search(r'Round\s*(\d+)', str(text))
    return int(m.group(1)) if m else 0

if 'round_name' in df.columns:
    unique_dates = sorted(df['round_name'].unique(), key=extract_round_num, reverse=True)
    
    pending_df = df[df['actual_winner'].isna() | (df['actual_winner'] == '')]
    default_idx = 0
    if not pending_df.empty:
        pending_rounds = sorted(pending_df['round_name'].unique(), key=extract_round_num, reverse=False)
        target_round = pending_rounds[0]
        if target_round in unique_dates:
            default_idx = unique_dates.index(target_round)
            
    selected_date = st.selectbox("Select Gameweek to inspect:", unique_dates, index=default_idx)
    filtered_df = df[df['round_name'] == selected_date].copy().reset_index(drop=True)
else:
    unique_dates = sorted(df['date'].unique(), reverse=True)
    selected_date = st.selectbox("Select Gameweek to inspect:", unique_dates, index=0)
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

    # Dashboard report dataframe
    display_df = pd.DataFrame()
    display_df['No.'] = filtered_df['day_no']
    display_df['Match Date (UK)'] = filtered_df['uk_date']
    display_df['Match Date (KST)'] = filtered_df['kst_date']
    display_df['Home Team'] = filtered_df.apply(lambda r: f"{r['home_team']} ({r['home_total_wuv']:.2f} WUV)" if ('home_total_wuv' in r and pd.notna(r.get('home_total_wuv'))) else (f"{r['home_team']} ({r['home_uv']:.2f} WUV)" if pd.notna(r.get('home_uv')) else r['home_team']), axis=1)
    display_df['Away Team'] = filtered_df.apply(lambda r: f"{r['visit_team']} ({r['visit_uv']:.2f} WUV)" if pd.notna(r.get('visit_uv')) else r['visit_team'], axis=1)
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

    st.dataframe(display_df, hide_index=True, use_container_width=True)



# -----------------------------------------------------------------------------
# 9. [최하단] 푸터 문구 (MLB/NBA 템플릿과 100% 동일)
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
