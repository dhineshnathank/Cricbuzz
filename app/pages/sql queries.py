import streamlit as st
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_connection import run_query

st.title("📊 SQL Analytics")

queries = {
    "Q1. Players who represent India": "select * from indian_player",
    "Q2. Recent matches (last few days)": "select * from recent_matches order by 1 desc",
    "Q3. Top 10 highest run scorers in ODI": "select * from mostruns_odi",
    "Q4. Venues with capacity > 25,000": "select * from bigger_venues",
    "Q5. Matches won by each team": "select * from matches_won order by 2 desc",
    "Q6. Player count by role": "select * from all_players",
    "Q7. Highest individual score by format": "select * from highest_scores",
    "Q8. Series started in 2024": "select * from series_list_2024",
    "Q9. All-rounders (1000+ runs, 50+ wickets)": "select * from allrounder_stats_table",
    "Q10. Last 20 completed matches": "select * from last_20_matches_table",
    "Q11. Player performance across formats": "select * from all_format_batt_stats",
    "Q13. Batting partnerships (100+ runs)": "select * from partnership",
    "Q14. Bowling performance by venue (Bumrah)": "select * from bumrah_data",
    "Q14b. Bowling performance by venue (Starc)": "select * from starc_data",
    "Q15. Player performance in close matches": "select * from close_match_data",
    "Q16. Yearly batting performance since 2020": "select * from rr_batt_stats",
    "Q17. Toss advantage analysis": "select * from rr_toss_data",
    "Q18. Economical bowlers (limited overs, AUS)": "select * from aus_bowl_stats",
    "Q19. Most consistent batsmen (std dev, AUS)": "select * from aus_std_deviation",
    "Q20. Bowling stats (India)": "select * from ind_bowl_stats",
    "Q21. Player ranking system": "select * from player_points_table",
    "Q22. Head-to-head analysis (CSK vs MI)": "select * from csk_mi_h2h",
    "Q23. Recent form & momentum (CSK)": "select * from csk_batt_table",
    "Q24. Successful batting partnerships": "select * from partnership_summary",
    "Q25. Career phase analysis": "select * from career_phase",
    "Extra. Team performance": "select * from team_performance",
    "Extra. Batting data": "select * from `batting data`",
}

choice = st.selectbox("Choose Query", list(queries.keys()))

try:
    df = run_query(queries[choice])
    df.index += 1
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Query failed: {e}")

st.markdown("---")
st.subheader("🛠️ Run a Custom Query")
custom_query = st.text_area("Write your own SELECT query:", height=100)
if st.button("Run Query"):
    if custom_query.strip().lower().startswith("select"):
        try:
            result_df = run_query(custom_query)
            st.dataframe(result_df, use_container_width=True)
        except Exception as e:
            st.error(f"Query failed: {e}")
    else:
        st.warning("Only SELECT queries are allowed here for safety.")