# US-Macroeconomics-Indicators-Pipeline
![Python](https://img.shields.io/badge/Python-3.12-blue)
![PySpark](https://img.shields.io/badge/PySpark-4.0-orange)
![Databricks](https://img.shields.io/badge/Databricks-Unity%20Catalog-red)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Gold-yellow)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![FRED API](https://img.shields.io/badge/FRED-API-green)
![CI](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/actions/workflows/ci.yml/badge.svg)


## Overview
This project is an end-to-end data engineering pipeline that ingests, processes, and analyzes economic data from the FRED API. 
Data is stored using the medallion architecture (Bronze, Silver, Gold) in Databricks Lakehouse with PySpark and Delta Lake.
A Logistic Regression model trained with MLflow predicts US recession probability with 92.5% accuracy. 
Results are visualized via Power BI and/ or a Databricks Dashboard, accessible through this Streamlit app. 
The pipeline runs automatically on the 1st Tuesday of every month, with email alerts for data quality issues and model drift detection.

## Architecture
FRED API

    -> Bronze Layer  (indicators, observations, ingestion_log, dq_log)
    
    -> Silver Layer  (wide_macro_indicators)
    
    -> Gold Layer    (annual_macro_summary, recession_periods, recession_predictions, monitoring_log)
    
    -> ML Model      (Logistic Regression, MLflow tracking)
    
    -> Monitoring    (drift detection, email alerts, retrain trigger)
    
    -> Visualization (Power BI, Databricks Dashboard, Streamlit)

## Tech Stack
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

## Data Sources
The datasource for this project is from the open source [FRED API](https://fredhelp.stlouisfed.org/fred/about/about-fred/what-is-fred/), which is actively maintained by the St Louis Federal Reserve. 
Here, we use 8 of the core indicators, namely:

| Sl No | Indicator | Description | Frequency |
|---|---|---|---|
| 1 | FEDFUNDS | Federal Funds Interest Rate | Monthly |
| 2 | CPIAUCSL | Consumer Price Index (Inflation) | Monthly |
| 3 | MORTGAGE30US | 30-Year Fixed Mortgage Rate | Weekly |
| 4 | UNRATE | Unemployment Rate | Monthly |
| 5 | DGS10 | 10-Year Treasury Yield | Daily |
| 6 | GDP | Gross Domestic Product | Quarterly |
| 7 | M2SL | M2 Money Supply | Monthly |
| 8 | USREC | US Recession Indicator | Monthly |

## Pipeline
The pipeline is orchestrated using Databricks Jobs & Pipelines and runs automatically on the 1st Tuesday of every month

| Task | Description |
|---|---|
| Bronze Ingestion | Pulls 8 FRED indicators via API, stores raw data in Delta tables with audit logging and DQ checks |
| Silver Transformation | Pivots observations into a wide table, adds recession flags and quarter start indicators |
| Gold Analytics | Computes annual summaries and recession periods |
| ML Inference | Runs recession probability predictions using saved MLflow model |
| Monitoring | Detects drift, sends email alerts, triggers retraining if needed |

## ML Model
A Logistic Regression model that is trained on 10 features which predicts monthly US recession probability

| Detail | Value |
|---|---|
| Algorithm | Logistic Regression (PySpark MLlib) |
| Features | FEDFUNDS, DGS10, UNRATE, MORTGAGE30US, yield_spread, M2SL, CPI + 3-month lags |
| Class Weight | 7.6x for recession months |
| AUC | 0.925 |
| Accuracy | 92.5% |
| Recall | 92.5% |
| Precision | 96.5% |
| Tracking | MLflow |

## Monitoring
Monitoring is setup to detect data drifts and data quality. An email is sent if either of the 2 takes place using the smtplib
python library.

## Dashboard
![Image 1 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/Databricks%20Dashboard%20Page%201.png)
![Image 2 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/Databricks%20Dashboard%20Page%202.png)
![Image 3 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/Databricks%20Dashboard%20Page%203.png)
![Image 4 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/Databricks%20Dashboard%20Page%204.png)
![Image 5 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/PBI%20Page%201.png)
![Image 6 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/PBI%20Page%202.png)
![Image 7 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/PBI%20Page%203.png)
![Image 8 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/dashboard_screenshots/PBI%20Page%204.png)

## Streamlit App
![Image 1 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/App%20Page.png)
![Image 2 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/Pipeline%20Status.png)
![Image 3 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/Pipeline%20Trigger.png)
![Image 4 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/Monitoring%20Page.png)
![Image 5 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/Dashboard%20Page.png)
![Image 6 alt text](https://github.com/pvvishwesh-lang/US-Macroeconomics-Indicators-Pipeline/blob/main/media/About%20Page.png)

## How to Run
1. Clone the repo
2. Get a free FRED API key at [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html)
3. Set up a Databricks workspace and create the Unity Catalog `us_macroeconomics_tracker`
4. Add your secrets to `.streamlit/secrets.toml`
6. Run the notebooks in order: `US_Macroeconomics_Tracker` -> `Recession_Predictor` -> `Gold_Model_Monitoring`
7. Install dependencies: `pip install -r app/requirements.txt`
8. Run the app: `streamlit run app/app.py`

## Key Findings
- **October 2023** saw the highest predicted recession probability (32%) coinciding with the 10-year Treasury yield hitting 5% for the first time since 2007
- **2020 COVID recession** was correctly predicted with high probability spikes in March-April 2020
- **2008 Financial Crisis** showed sustained high recession probabilities from late 2007 through 2009
- **Current recession risk (Jan 2026)** is very low at 0.33%, suggesting stable economic conditions
- **92.5% model accuracy** with only 48 misclassifications out of 654 historical months

## Future Improvements
- Add more economic indicators (PCE, housing starts, consumer confidence)
- Experiment with ensemble models (Random Forest, XGBoost) and Hyperparameter Tuning
- Build a REST API layer using FastAPI to create a more interactive web application
- Add real-time streaming with Apache Kafka
