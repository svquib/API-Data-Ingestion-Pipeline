import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv
from extract import fetch_repositories
from transform import transform_repositories
from load import load_to_bigquery

load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET = os.getenv("BQ_DATASET")
PIPELINE_NAME = "github_repos_spotify"

def get_last_updated_timestamp():
    client = bigquery.Client(project=PROJECT_ID)
    
    query = f"""
        SELECT MAX(last_updated_at) as last_ts
        FROM `{PROJECT_ID}.{DATASET}.ingestion_metadata`
        WHERE pipeline_name = '{PIPELINE_NAME}'
    """
    result = client.query(query).result()
    for row in result:
        return row.last_ts
    return None

def update_last_updated_timestamp(ts):
    """Replaces the metadata table row with the new watermark (Free-Tier friendly)."""
    client = bigquery.Client(project=PROJECT_ID)
    table_id = f"{PROJECT_ID}.{DATASET}.ingestion_metadata"

    
    new_state = pd.DataFrame([{
        "pipeline_name": PIPELINE_NAME,
        "last_updated_at": ts,
        "updated_at": pd.Timestamp.now(tz='UTC')
    }])

    
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    client.load_table_from_dataframe(new_state, table_id, job_config=job_config).result()
    print(f"🔄 Watermark updated to: {ts}")

def run():
    print("🚀 Starting Incremental Pipeline...")
    last_updated = get_last_updated_timestamp()
    print(f"📅 Last ingestion watermark: {last_updated}")
    
    repos = fetch_repositories(last_updated)

    if not repos:
        print("✅ No new repositories since last run.")
        return

    df = transform_repositories(repos)
    load_to_bigquery(df)

    
    max_updated = df["updated_at"].max()
    update_last_updated_timestamp(max_updated)

    print(f"✨ Successfully ingested {len(df)} repositories.")

if __name__ == "__main__":
    run()