import streamlit as st
from databricks.sdk import WorkspaceClient
import streamlit.components.v1 as components
import os
os.environ.pop("DATABRICKS_TOKEN", None)

dashboard_url = os.getenv("DASHBOARD_URL")

st.title("Dashboard")
st.markdown("View the live Databricks dashboard below:")

token = os.environ.pop("DATABRICKS_TOKEN", None)
if "client" not in st.session_state:
    st.session_state.client = WorkspaceClient(host=os.getenv("DATABRICKS_HOST")
        #host=st.secrets["DATABRICKS_HOST"],token=st.secrets["DATABRICKS_TOKEN"]
    )
if token:
    os.environ["DATABRICKS_TOKEN"] = token


components.iframe(dashboard_url , height=800, scrolling=True) #st.secrets["DASHBOARD_URL"]
st.info("If the dashboard doesn't load, click here to open it directly.")
st.link_button("Open Dashboard", dashboard_url)#st.secrets["DASHBOARD_URL"]
