import streamlit as st
from databricks.sdk import WorkspaceClient
import os
st.title("Trigger Pipeline")

st.markdown("""
Click the button below to trigger the pipeline manually.
You can monitor the pipeline status and view logs by navigating to the Pipeline_Status and Monitoring Log pages.
""")


if "client" not in st.session_state:
    st.session_state.client = WorkspaceClient(host=os.getenv("DATABRICKS_HOST")
        #host=st.secrets["DATABRICKS_HOST"],token=st.secrets["DATABRICKS_TOKEN"]
    )

button=st.button("Run Pipeline")
if button:
    try:
        with st.spinner("Triggering pipeline..."):
            st.session_state.client.jobs.run_now(job_id=os.getenv("JOB_ID"))
            st.success("Pipeline triggered successfully!")
        runs = list(st.session_state.client.jobs.list_runs(job_id=os.getenv("JOB_ID"), limit=1))
        if runs:
            latest_run = runs[0]
            run_id=latest_run.run_id
            st.markdown(f"Latest Run ID: {run_id}")
    except Exception as e:
        st.error(f"Error fetching latest run: {e}")
