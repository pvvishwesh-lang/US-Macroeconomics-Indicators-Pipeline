import streamlit as st
from databricks.sdk import WorkspaceClient
from datetime import datetime
import pandas as pd
import time
st.title("Pipeline Status")

if st.button("Refresh"):
    st.rerun()

if "client" not in st.session_state:
    st.session_state.client = WorkspaceClient(
        host=st.secrets["DATABRICKS_HOST"],
        token=st.secrets["DATABRICKS_TOKEN"]
    )
with st.spinner("Fetching latest run..."):
    runs = list(st.session_state.client.jobs.list_runs(job_id=st.secrets["JOB_ID"], limit=10))
    if runs:
        latest_run = runs[0]
        status = str(latest_run.state.life_cycle_state).split(".")[-1]   
        if status == "RUNNING":
            st.info("Pipeline is currently running. Page will refresh in 30 seconds.")
            time.sleep(30)
            st.rerun()
        result_state= str(latest_run.state.result_state).split(".")[-1]
        starttime = datetime.fromtimestamp(latest_run.start_time/1000).strftime("%Y-%m-%d %H:%M:%S")
        duration=round(latest_run.execution_duration/60000,1)
        run_id=latest_run.run_id
        col1, col2, col3, col4,col5 = st.columns(5)
        if result_state == "SUCCESS":
            col1.success(result_state)
        else:
            col1.error(result_state)
        col2.metric(label="Start Time", value=starttime)
        col3.metric(label="Duration", value=duration)
        col4.metric(label="Run ID", value=run_id)
        col5.metric(label="Status", value=status)
    else:
        st.markdown("No pipeline runs found.")
    st.subheader('Run History')
    history=[]
    for run in runs:
        history.append({
        "Run ID": run.run_id,
        "Result": str(run.state.result_state).split(".")[-1],
        "Status": str(run.state.life_cycle_state).split(".")[-1],
        "Start Time": datetime.fromtimestamp(run.start_time/1000).strftime("%Y-%m-%d %H:%M:%S"),
        "Duration (mins)": round(run.execution_duration/60000, 1)
    })
    st.dataframe(pd.DataFrame(history))
