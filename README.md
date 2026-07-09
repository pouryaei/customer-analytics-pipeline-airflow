# Customer Analytics Pipeline with Apache Airflow

A production-inspired **Customer Analytics Pipeline** built with **Apache Airflow 3.2.2** to demonstrate modern Data Engineering workflows, ETL orchestration, Machine Learning integration, and production best practices.

This project is designed as a portfolio project for GitHub, technical interviews, and the Axiomeet website.

---

## Project Goals

The pipeline automates a complete customer analytics workflow:

* Extract customer transaction data
* Validate incoming data
* Clean and transform datasets
* Perform feature engineering
* Store processed data locally (Parquet)
* Load data into PostgreSQL
* Train a Machine Learning model
* Track experiments using MLflow
* Generate an automated analytics report
* Archive processed files

Apache Airflow orchestrates the entire workflow.

---

## Dataset

* **Online Retail II**

---

## Technology Stack

* Python 3.11
* Apache Airflow 3.2.2
* Pandas
* PyArrow
* PostgreSQL
* Scikit-learn
* MLflow
* Docker

---

## Project Structure

```text
airflow/
├── dags/
├── logs/
├── plugins/

docker/

docs/

scripts/

src/
└── customer_data_platform/

tests/
```

---

## Planned Pipeline

```text
Extract
    ↓
Validate
    ↓
Clean
    ↓
Feature Engineering
    ↓
Save Local (Parquet)
    ↓
Load PostgreSQL
    ↓
Train Model
    ↓
Track with MLflow
    ↓
Generate Report
    ↓
Archive Raw Files
```

---

## Project Roadmap

* ✅ Phase 1 — Environment Setup
* 🚧 Phase 2 — Airflow Fundamentals
* ⏳ Phase 3 — Data Ingestion & Validation
* ⏳ Phase 4 — ETL & Feature Engineering
* ⏳ Phase 5 — PostgreSQL Integration
* ⏳ Phase 6 — Machine Learning & MLflow
* ⏳ Phase 7 — Docker & Production Packaging

---

## Objectives

This project focuses on learning and demonstrating:

* Apache Airflow
* Production-style ETL pipelines
* Data validation
* Feature engineering
* PostgreSQL integration
* Machine Learning orchestration
* MLflow experiment tracking
* Docker-based deployment
* Production best practices

---

## License

This project is intended for educational and portfolio purposes.
