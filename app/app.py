import streamlit as st
from databricks.sdk import WorkspaceClient

st.set_page_config(page_title="US Macroeconomic Pipeline", page_icon="📊", layout="wide")

if "client" not in st.session_state:
    st.session_state.client = WorkspaceClient(
        host=st.secrets["DATABRICKS_HOST"],
        token=st.secrets["DATABRICKS_TOKEN"]
    )

st.title("US Macroeconomic Indicators Pipeline")
st.markdown("An end to end data engineering and ML pipeline built on Databricks using PySpark, ingesting Federal Reserve economic data from FRED API.")

st.markdown("### Navigate using the sidebar to:")
st.markdown("- View pipeline status\n- Trigger the pipeline manually\n- View monitoring log\n- View dashboard")

st.sidebar.markdown("### About")
st.sidebar.markdown("**US Macroeconomic Indicators Pipeline**")
st.sidebar.markdown("End to end data engineering and ML pipeline built on Databricks.")
st.sidebar.divider()
st.sidebar.markdown("### Links")
st.sidebar.markdown("[GitHub](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/vishwesh-p-v)")
st.sidebar.divider()
st.sidebar.markdown("### Tech Stack")
st.sidebar.markdown("PySpark · Delta Lake · MLflow · FRED API · Databricks · Streamlit")



