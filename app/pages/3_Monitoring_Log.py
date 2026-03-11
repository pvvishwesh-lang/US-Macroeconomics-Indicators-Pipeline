import streamlit as st
from databricks.sdk import WorkspaceClient
from databricks import sql
import pandas as pd
from datetime import datetime
import os
host = os.getenv("DATABRICKS_HOST").replace("https://","")
token = os.getenv("DATABRICKS_TOKEN")
http_path = os.getenv("HTTP_PATH")

st.title("Monitoring Log")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if "client" not in st.session_state:
    st.session_state.client = WorkspaceClient(
       # host=st.secrets["DATABRICKS_HOST"],token=st.secrets["DATABRICKS_TOKEN"]
    )
@st.cache_data(ttl=600)
def get_monitoring_data():
    conn = sql.connect(
    server_hostname=host, #st.secret["DATABRICKS_HOST"].replace("https://","")
    http_path=http_path, #st.secret["HTTP_PATH"]
    access_token=token #st.secret["DATABRICKS_TOKEN"]
    )

    QUERY="SELECT * FROM us_macroeconomics_tracker.gold.monitoring_log ORDER BY obs_date DESC"
    cursor = conn.cursor()

    cursor.execute(QUERY)
    results = cursor.fetchall()
    cols=cursor.description
    col_names = [col[0] for col in cols]
    df = pd.DataFrame(results, columns=col_names)
    conn.close()
    return df
if st.button("Refresh"):
    st.cache_data.clear()

df=get_monitoring_data()
st.dataframe(df)

drift_count = df[df['drift_flag'] == True].shape[0]
st.metric(label="Drift Flags Detected", value=drift_count)
