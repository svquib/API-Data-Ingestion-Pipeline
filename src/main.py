import sys
from dotenv import load_dotenv
from extract import fetch_repositories
from transform import transform_repositories
from load import load_to_bigquery


load_dotenv()

def get_last_updated_timestamp():
    """
    In a future step, this will query BigQuery to find the 
    most recent 'updated_at' date to perform an incremental load.
    """
    return None

def run():
    print("🚀 Pipeline Started...")
    
    try:
        
        last_updated = get_last_updated_timestamp()

        
        print("🛰️  Fetching repositories from GitHub...")
        repos = fetch_repositories(last_updated)

        if not repos:
            print("🛑 No new repositories found. Exiting.")
            return

        
        print(f"🛠️  Transforming {len(repos)} records...")
        df = transform_repositories(repos)

        
        print("📤 Uploading data to BigQuery...")
        load_to_bigquery(df)

        print(f"✅ Success! Ingested {len(df)} repositories.")

    except Exception as e:
        
        print(f"❌ Pipeline failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()