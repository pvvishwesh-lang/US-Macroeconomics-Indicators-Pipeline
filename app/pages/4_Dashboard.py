import streamlit as st
from databricks.sdk import WorkspaceClient
import streamlit.components.v1 as components
import os
dashboard_url = os.getenv("DASHBOARD_URL")

st.title("Dashboard")
st.markdown("View the live Databricks dashboard below:")


if "client" not in st.session_state:
    st.session_state.client = WorkspaceClient(
        #host=st.secrets["DATABRICKS_HOST"],token=st.secrets["DATABRICKS_TOKEN"]
    )


components.iframe(dashboard_url , height=800, scrolling=True) #st.secrets["DASHBOARD_URL"]
st.info("If the dashboard doesn't load, click here to open it directly.")
st.link_button("Open Dashboard", dashboard_url #st.secrets["DASHBOARD_URL"])
