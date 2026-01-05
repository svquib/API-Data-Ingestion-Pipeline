# 🚀 API Data Ingestion Pipeline

### 📌 Project Overview
This project implements a production-style API data ingestion pipeline that ingests repository metadata from the **GitHub REST API** for the Spotify organization, performs incremental updates using a metadata watermark strategy, and loads the data into **Google BigQuery** for analytics and reporting.

### 🏗️ Architecture
**GitHub REST API** → **Python Ingestion Layer** → **Incremental Processing** → **BigQuery**
* **Orchestration:** Apache Airflow (Dockerized)

### 🧰 Tech Stack
* **Language:** Python 3
* **API:** GitHub REST API v3
* **Cloud Platform:** Google Cloud Platform (GCP)
* **Data Warehouse:** BigQuery
* **Orchestration:** Apache Airflow
* **Containerization:** Docker
* **Libraries:** `requests`, `pandas`, `google-cloud-bigquery`

### 📁 Repository Structure

```text
API-DATA-INGESTION-PIPELINE/
├── airflow/
│   ├── dags/
│   │   └── github_ingestion_dag.py
│   ├── docker-compose.yaml
│   └── logs/
├── config/
│   └── service-account-key.json
├── sql/
│   ├── ingestion_metadata.sql
│   └── repositories.sql
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── .env
├── .gitignore
├── init_metadata.csv
├── requirements.txt
└── README.md

▶️ How to Run

    Configure environment variables: Create a .env file in the root.

    Activate Environment: source venv/bin/activate (or your local equivalent).

    Run locally:
    Bash

python src/main.py

Orchestrate with Airflow:
Bash

    docker-compose up -d

📈 What I Learned

    Designing scalable API ingestion pipelines.

    Implementing incremental data processing using watermarks.

    Using BigQuery as both storage and pipeline state manager.

    Orchestrating workflows with Apache Airflow.

    Applying production-ready cloud IAM and security practices.
