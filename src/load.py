import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv


load_dotenv()


PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET = os.getenv("BQ_DATASET")
TABLE = "repositories"

KEY_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "config/service-account-key.json")

def load_to_bigquery(df):
    """Loads a pandas DataFrame to BigQuery with proper auth and error handling."""
    
    if df.empty:
        print("⚠️ DataFrame is empty. Skipping load.")
        return

    try:
        
        credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
        client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
        
        table_id = f"{PROJECT_ID}.{DATASET}.{TABLE}"

        
        job_config = bigquery.LoadJobConfig(
            
            write_disposition="WRITE_APPEND",
            
            autodetect=True,
        )

        print(f"📥 Loading {len(df)} rows to {table_id}...")
        
        
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        
        
        job.result()
        
        print(f"✅ Successfully loaded data to BigQuery.")

    except Exception as e:
        print(f"❌ BigQuery Load Error: {e}")