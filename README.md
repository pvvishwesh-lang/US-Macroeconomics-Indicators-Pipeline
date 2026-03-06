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


## Pipeline


## ML Model


## Monitoring


## Dashboard


## Streamlit App


## How to Run


## Key Findings


## Future Improvements

