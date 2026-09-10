import os
import sqlite3
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "bdl_data.db")

st.set_page_config(


    page_title="Bundesliga AI Match Predictor",
    page_icon="⚽",
    layout="wide"
)

from common_nav import render_common_nav
render_common_nav("BDL")






st.divider()

st.title("⚽ Bundesliga AI Match Predictor")

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
            if "match_date_ger" in df_db.columns:
                df_db["ger_date"] = df_db["match_date_ger"]
            else:
                df_db["ger_date"] = df_db.get("date", df_db.get("match_date", "2026-08"))
            if "match_date_kst" in df_db.columns:
                df_db["kst_date"] = df_db["match_date_kst"]
            else:
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
        "total_no", "date", "ger_date", "kst_date", "round_name", "home_team", "visit_team",
        "predicted_winner", "predicted_gap", "prob_home", "prob_draw", "prob_away",
        "home_uv", "visit_uv", "actual_winner", "actual_score_home", "actual_score_away", "is_correct"
    ])
    stats_df = pd.DataFrame([])

# -----------------------------------------------------------------------------
# 5. Cumulative Prediction Scorecard
# -----------------------------------------------------------------------------
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
# 6. Prediction Scorecard by Round (Bundesliga Gameweek)
# -----------------------------------------------------------------------------
st.header("📈 Prediction Scorecard by Round (Bundesliga Gameweek)")

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

    round_stats_7d = round_stats.tail(10)

    base = alt.Chart(round_stats_7d).encode(x=alt.X(group_col, title='Bundesliga Gameweek', sort=None))
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
# 7. Gameweek Match Report (9 Matchups)
# -----------------------------------------------------------------------------
st.header("📋 Gameweek Match Report (9 Matchups)")

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

    display_df = pd.DataFrame()
    display_df['No.'] = filtered_df['day_no']
    display_df['Match Date (GER)'] = filtered_df.apply(lambda r: r['ger_date'] if ('ger_date' in r and pd.notna(r['ger_date'])) else r.get('match_date_ger', r.get('match_date', '')), axis=1)
    display_df['Match Date (KST)'] = filtered_df.apply(lambda r: r['kst_date'] if ('kst_date' in r and pd.notna(r['kst_date'])) else r.get('match_date_kst', r.get('match_date', '')), axis=1)
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

    st.dataframe(display_df, hide_index=True, width='stretch')

# -----------------------------------------------------------------------------
# 9. [최하단] 푸터 문구
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