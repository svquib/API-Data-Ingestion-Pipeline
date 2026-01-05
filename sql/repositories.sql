CREATE TABLE IF NOT EXISTS `github_analytics.repositories` (
  repo_id INT64,
  name STRING,
  owner STRING,
  description STRING,
  language STRING,
  stargazers_count INT64,
  forks_count INT64,
  open_issues_count INT64,
  updated_at TIMESTAMP,
  ingestion_timestamp TIMESTAMP
);
