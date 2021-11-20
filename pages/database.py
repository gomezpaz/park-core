import streamlit as st
from streamlit_autorefresh import st_autorefresh
from gsheetsdb import connect
import pandas as pd


def app():
    st.header("Database")
    # Create a connection object.
    conn = connect()

    # Perform SQL query on the Google Sheet.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    # @st.cache(ttl=600)

    st_autorefresh(interval=1000, limit=1000000, key="updatetable")

    def run_query(query):
        rows = conn.execute(query, headers=1)
        return rows

    sheet_url = st.secrets["public_gsheets_url"]
    rows = run_query(f'SELECT * FROM "{sheet_url}"')

    table = pd.DataFrame(rows)
    st.table(table)
