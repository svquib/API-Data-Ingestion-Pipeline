import os
import time
import requests
from datetime import datetime
from dateutil import parser

from dotenv import load_dotenv


load_dotenv() 


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ORG = os.getenv("GITHUB_ORG", "spotify") 

HEADERS = {
    
    "Authorization": f"Bearer {GITHUB_TOKEN}", 
    "Accept": "application/vnd.github.v3+json"
}


def get_base_url():
    return f"https://api.github.com/orgs/{os.getenv('GITHUB_ORG', 'spotify')}/repos"

def fetch_repositories(since_timestamp=None):
    repos = []
    page = 1
    base_url = get_base_url() 

    while True:
        params = {
            "per_page": 100,
            "page": page,
            "sort": "updated"
        }

        print(f"📡 Requesting: {base_url} (Page {page})") 
        response = requests.get(base_url, headers=HEADERS, params=params)

        if response.status_code == 403:
            print("⏳ Rate limit hit. Sleeping for 60 seconds.")
            time.sleep(60)
            continue

        response.raise_for_status()
        data = response.json()

        if not data:
            break

        for repo in data:
            updated_at = parser.parse(repo["updated_at"])
            
            if since_timestamp and updated_at <= since_timestamp:
                return repos
            repos.append(repo)

        page += 1

    return repos