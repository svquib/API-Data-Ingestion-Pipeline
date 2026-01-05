import pandas as pd
from datetime import datetime

def transform_repositories(repos):
    """
    Cleans and structures GitHub API data for BigQuery.
    """
    if not repos:
        return pd.DataFrame()

    records = []

    for r in repos:
        records.append({
            "repo_id": r["id"],
            "name": r["name"],
            
            "owner": r["owner"].get("login"),
            "description": r.get("description"),
            "language": r.get("language"),
            "stargazers_count": r.get("stargazers_count", 0),
            "forks_count": r.get("forks_count", 0),
            "open_issues_count": r.get("open_issues_count", 0),
            "updated_at": r.get("updated_at"),
            "ingestion_timestamp": datetime.utcnow()
        })

    df = pd.DataFrame(records)

    
    if 'updated_at' in df.columns:
        df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')

    
    df = df.where(pd.notnull(df), None)

    return df