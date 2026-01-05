📌 Project Overview

This project implements a production-style API data ingestion pipeline that ingests repository metadata from the GitHub REST API for the Spotify organization, performs incremental updates using a metadata watermark strategy, and loads the data into Google BigQuery for analytics and reporting.

The pipeline is designed to reflect real-world data engineering workflows, including secure authentication, pagination handling, incremental ingestion, cloud-native storage, and orchestration using Apache Airflow.

🏗️ Architecture

GitHub REST API → Python Ingestion Layer → Incremental Processing → BigQuery → Analytics

Orchestration: Apache Airflow (Dockerized)

🧰 Tech Stack

Language: Python 3

API: GitHub REST API v3

Cloud Platform: Google Cloud Platform (GCP)

Data Warehouse: BigQuery

Orchestration: Apache Airflow

Containerization: Docker

Libraries: requests, pandas, google-cloud-bigquery

🔁 Key Features

API authentication using GitHub tokens

Pagination and rate-limit handling

Incremental ingestion using BigQuery metadata watermark table

Idempotent data loading into BigQuery

Airflow DAG for scheduling and retries

Secure service account-based cloud authentication

📂 Repository Structure
API-DATA-INGESTION-PIPELINE/
├── airflow/
│   └── dags/
│       └── github_ingestion_dag.py
│
├── config/
│   └── service-account-key.json
│
├── sql/
│   ├── ingestion_metadata.sql
│   └── repositories.sql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── docker-compose.yaml
├── init_metadata.csv
├── requirements.txt
├── .env
├── .gitignore
└── README.md

▶️ How to Run

Configure environment variables (.env)

Activate Python virtual environment

Run locally:

python src/main.py

Orchestrate with Airflow:

docker compose up -d
📊 Sample Analytics

Repository count by language

Star and fork distribution

Recently updated repositories

📈 What I Learned

Designing scalable API ingestion pipelines

Implementing incremental data processing using watermarks

Using BigQuery as both storage and pipeline state manager

Orchestrating workflows with Apache Airflow

Applying production-ready cloud IAM and security practices
