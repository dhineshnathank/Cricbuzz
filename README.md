# Cricbuzz LiveStats — Real-Time Cricket Insights & SQL-Based Analytics

A Streamlit dashboard that combines live cricket data from the Cricbuzz API with SQL-based analytics on a MySQL backend. Built as a capstone project in the sports analytics domain.

## Features

- **Live Matches** — Real-time match and scorecard data pulled from the Cricbuzz API
- **Top Player Stats** — Player search/autocomplete with batting and bowling career stats, plus a top-stats ranking table with format and stat-type selectors
- **SQL Analytics** — 25 SQL practice queries run against real match, player, and team data
- **CRUD Operations** — Create, Read, Update, and Delete player records in the `all_players` table

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **Database:** MySQL (via SQLAlchemy + mysql-connector)
- **Data Source:** Cricbuzz Cricket API (RapidAPI)

## Project Structure

```
Cricbuzz/
├── app/
│   ├── Home.py
│   └── pages/
│       ├── sql_queries.py
│       ├── live_matches.py
│       ├── top_player_stats.py
│       └── crud_operations.py
├── utils/
│   ├── __init__.py
│   └── db_connection.py
├── .env.cricbuzz
└── README.md
```

## Database

MySQL database `CricBuzz` with tables covering batting/bowling stats, match data, team performance, player records, and more — including `all_format_batt_stats`, `all_players`, `career_phase`, `partnership`, `team_performance`, and others.

## Status

All four dashboard pages are complete and tested: SQL Analytics, Live Matches, Top Player Stats, and CRUD Operations.
