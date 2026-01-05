from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os


sys.path.append("/opt/airflow/src")

def run_ingestion_wrapper():
    """
    Importing inside the function ensures that the Scheduler 
    doesn't fail if the libraries are still loading.
    """
    from main import run  
    return run()

default_args = {
    "owner": "airflow",
    "retries": 1,
}

with DAG(
    dag_id="github_spotify_ingestion",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["spotify", "github"]
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_github_repos",
        python_callable=run_ingestion_wrapper  
    )