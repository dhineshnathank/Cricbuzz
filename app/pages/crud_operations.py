import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st  # noqa: E402
import pandas as pd  # noqa: E402
from utils.db_connection import run_query, execute_statement  # noqa: E402


def is_valid_text(value):
    return isinstance(value, str) and value.strip() != ""


st.title("🛠 CRUD Operations")

mode = st.radio(
    "Choose Action",
    ["Create", "Read", "Update", "Delete"],
    horizontal=True
)

ROLES = ["BATSMEN", "BOWLER", "ALL ROUNDER", "WK-BATSMEN"]

# -----------------------------
# CREATE
# -----------------------------
if mode == "Create":
    st.subheader("➕ Add Player")

    team_id = st.number_input("Team ID", min_value=0, step=1)
    team_name = st.text_input("Team Name")
    player_id = st.number_input("Player ID", min_value=0, step=1)
    player_name = st.text_input("Player Name")
    role = st.selectbox("Role", ROLES)
    batting_style = st.text_input("Batting Style")
    bowling_style = st.text_input("Bowling Style")

    if st.button("Add Player"):
        if not is_valid_text(player_name):
            st.error("❌ Player Name must be text")
        elif not is_valid_text(team_name):
            st.error("❌ Team Name must be text")
        else:
            try:
                execute_statement(
                    """
                    INSERT INTO all_players
                        (`Team ID`, `Team Name`, `Player ID`, `Player Name`, `Role`, `Batting Style`, `Bowling Style`)
                    VALUES
                        (:team_id, :team_name, :player_id, :player_name, :role, :batting_style, :bowling_style)
                    """,
                    {
                        "team_id": team_id,
                        "team_name": team_name.strip(),
                        "player_id": player_id,
                        "player_name": player_name.strip(),
                        "role": role,
                        "batting_style": batting_style.strip(),
                        "bowling_style": bowling_style.strip(),
                    }
                )
                st.success("✅ Player added successfully!")
            except Exception as e:
                st.error(f"❌ Failed to add player: {e}")

# -----------------------------
# READ
# -----------------------------
elif mode == "Read":
    st.subheader("📄 All Players")

    try:
        df = run_query("SELECT * FROM all_players")
        df.index += 1
        st.dataframe(df, width="stretch")
    except Exception as e:
        st.error(f"❌ Failed to load players: {e}")

# -----------------------------
# UPDATE
# -----------------------------
elif mode == "Update":
    st.subheader("✏️ Update Player")

    try:
        players_df = run_query("SELECT * FROM all_players")
    except Exception as e:
        st.error(f"❌ Failed to load players: {e}")
        st.stop()

    if players_df.empty:
        st.warning("No players found")
        st.stop()

    labels = [
        f"{row['Player Name']} ({row['Team Name']}) - ID {row['Player ID']}"
        for _, row in players_df.iterrows()
    ]
    selected = st.selectbox("Select Player", labels)
    idx = labels.index(selected)
    old = players_df.iloc[idx]

    team_id = st.number_input("Team ID", value=int(
        old["Team ID"]), min_value=0, step=1)
    team_name = st.text_input("Team Name", old["Team Name"])
    player_name = st.text_input("Player Name", old["Player Name"])
    role = st.selectbox("Role", ROLES, index=ROLES.index(
        old["Role"]) if old["Role"] in ROLES else 0)
    batting_style = st.text_input("Batting Style", old["Batting Style"])
    bowling_style = st.text_input("Bowling Style", old["Bowling Style"])

    if st.button("Update Player"):
        if not is_valid_text(player_name):
            st.error("❌ Player Name must be text")
        elif not is_valid_text(team_name):
            st.error("❌ Team Name must be text")
        else:
            try:
                execute_statement(
                    """
                    UPDATE all_players
                    SET `Team ID`=:team_id, `Team Name`=:team_name, `Player Name`=:player_name,
                        `Role`=:role, `Batting Style`=:batting_style, `Bowling Style`=:bowling_style
                    WHERE `Player ID`=:player_id
                    """,
                    {
                        "team_id": team_id,
                        "team_name": team_name.strip(),
                        "player_name": player_name.strip(),
                        "role": role,
                        "batting_style": batting_style.strip(),
                        "bowling_style": bowling_style.strip(),
                        "player_id": int(old["Player ID"]),
                    }
                )
                st.success("✅ Player updated successfully!")
            except Exception as e:
                st.error(f"❌ Failed to update player: {e}")

# -----------------------------
# DELETE
# -----------------------------
elif mode == "Delete":
    st.subheader("🗑 Delete Player")

    try:
        players_df = run_query("SELECT * FROM all_players")
    except Exception as e:
        st.error(f"❌ Failed to load players: {e}")
        st.stop()

    if players_df.empty:
        st.warning("No players available")
        st.stop()

    labels = [
        f"{row['Player Name']} ({row['Team Name']}) - ID {row['Player ID']}"
        for _, row in players_df.iterrows()
    ]
    selected = st.selectbox("Select Player to Delete", labels)
    idx = labels.index(selected)
    player_id = int(players_df.iloc[idx]["Player ID"])

    if st.button("Delete Player"):
        try:
            execute_statement(
                "DELETE FROM all_players WHERE `Player ID`=:player_id",
                {"player_id": player_id}
            )
            st.success("❌ Player deleted")
        except Exception as e:
            st.error(f"❌ Failed to delete player: {e}")
