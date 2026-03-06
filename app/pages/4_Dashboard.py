import streamlit as st
from databricks.sdk import WorkspaceClient
import streamlit.components.v1 as components


st.title("Dashboard")
st.markdown("View the live Databricks dashboard below:")


if "client" not in st.session_state:
    st.session_state.client = WorkspaceClient(
        host=st.secrets["DATABRICKS_HOST"],
        token=st.secrets["DATABRICKS_TOKEN"]
    )


components.iframe(st.secrets["DASHBOARD_URL"], height=800, scrolling=True)
st.info("If the dashboard doesn't load, click here to open it directly.")
st.link_button("Open Dashboard", st.secrets["DASHBOARD_URL"])
