import streamlit as st
from databricks import sql
import pandas as pd
import os
os.environ.pop("DATABRICKS_TOKEN", None)

st.title("About")

st.subheader("Project Overview ")
st.write("" \
    "This project is an end-to-end data engineering pipeline that ingests, processes, and analyzes "
    "economic data from the FRED API. Data is stored using the medallion architecture (Bronze, Silver, Gold) "
    "in Databricks Lakehouse with PySpark and Delta Lake. A Logistic Regression model trained with MLflow "
    "predicts US recession probability with 92.5% accuracy. Results are visualized via Power BI and/ or a "
    "Databricks Dashboard, accessible through this Streamlit app. The pipeline runs automatically on the "
    "1st Tuesday of every month, with email alerts for data quality issues and model drift detection."
)

st.subheader("Architecture")
st.code("""
FRED API
    -> Bronze Layer  (indicators, observations, ingestion_log, dq_log)
    -> Silver Layer  (wide_macro_indicators)
    -> Gold Layer    (annual_macro_summary, recession_periods, recession_predictions, monitoring_log)
    -> ML Model      (Logistic Regression, MLflow tracking)
    -> Monitoring    (drift detection, email alerts, retrain trigger)
    -> Visualization (Power BI, Databricks Dashboard, Streamlit)
""")

st.subheader("Tech Stack")
st.markdown("""
| Category | Tools |
|---|---|
| Cloud & Storage | Databricks, Delta Lake, Unity Catalog |
| Processing | PySpark, Apache Spark |
| ML & Tracking | Scikit-Learn, MLflow |
| Orchestration | Databricks Workflows |
| Data Source | FRED API |
| Visualization | Power BI, Databricks Dashboard |
| App | Streamlit |
| CI/CD | GitHub Actions |
""")


@st.cache_data(ttl=600)
def get_key_findings():
    conn = sql.connect(
    server_hostname=os.getenv("DATABRICKS_HOST").replace("https://",""), #st.secret["DATABRICKS_HOST"].replace("https://","")
    http_path=os.getenv("HTTP_PATH"), #st.secret['DATABRICKS_TOKEN']
    access_token=os.getenv("DATABRICKS_TOKEN") #st.secret['HTTP_PATH']
    )
    QUERY1="SELECT obs_date, recession_probability FROM us_macroeconomics_tracker.gold.recession_predictions ORDER BY obs_date DESC LIMIT 1"
    QUERY2="SELECT obs_date, recession_probability FROM us_macroeconomics_tracker.gold.recession_predictions ORDER BY recession_probability DESC LIMIT 1"
    QUERY3 = "SELECT count(*) as recession_count FROM us_macroeconomics_tracker.gold.recession_predictions WHERE is_recession_predicted = 1"
    cursor = conn.cursor()
    cursor.execute(QUERY1)
    results1 = cursor.fetchall()
    cols1=cursor.description
    cursor.execute(QUERY2)
    results2 = cursor.fetchall()
    cols2=cursor.description
    cursor.execute(QUERY3)
    results3 = cursor.fetchall()
    cols3=cursor.description
    col_names1 = [col[0] for col in cols1]
    col_names2 = [col[0] for col in cols2]
    col_names3 = [col[0] for col in cols3]
    df1 = pd.DataFrame(results1, columns=col_names1)
    df2 = pd.DataFrame(results2, columns=col_names2)
    df3 = pd.DataFrame(results3, columns=col_names3)
    conn.close()
    return df1, df2, df3
df_latest, df_highest,df_count = get_key_findings()
latest_prob = df_latest['recession_probability'].iloc[0]
latest_date = df_latest['obs_date'].iloc[0]
highest_prob = df_highest['recession_probability'].iloc[0]
highest_date = df_highest['obs_date'].iloc[0]
recession_count = df_count['recession_count'].iloc[0]

st.subheader("Key Findings")
st.markdown(f"- **Latest recession probability** ({latest_date}): {round(latest_prob*100, 2)}%")
st.markdown(f"- **Highest ever predicted probability** ({highest_date}): {round(highest_prob*100, 2)}%")
st.markdown(f"- **Total recession months predicted since 1971**: {recession_count}")
st.markdown("- **Model accuracy**: 92.5% (AUC: 0.925)")

st.subheader("Links")
st.markdown("[GitHub Repository](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline)")
st.markdown("[LinkedIn](https://www.linkedin.com/in/vishwesh-p-v)")
