import streamlit as st

st.set_page_config(page_title="Cricbuzz LiveStats", page_icon="🏏", layout="wide")

st.title("🏏 Cricbuzz LiveStats")
st.markdown("### Real-Time Cricket Insights & SQL-Based Analytics")

st.markdown("""
Welcome to the Cricbuzz LiveStats dashboard — a comprehensive cricket analytics platform combining
live match data from the Cricbuzz API with SQL-driven insights from a MySQL database.

**Use the sidebar to navigate:**
- 📊 **SQL Analytics** — explore results from 25 cricket analytics queries
- 🏏 **Live Matches** — real-time scores and match info *(coming soon)*
- 👤 **Player Stats** — top batting and bowling statistics *(coming soon)*
- 🛠️ **CRUD Operations** — manage player and match records *(coming soon)*

Built with Python, Streamlit, SQL, and REST API integration.
""")