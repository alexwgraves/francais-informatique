-- this query took 52.8 seconds to run on Google BigQuery, processing 2.5 TB of data
SELECT b.path AS file, c.content AS content, a.country_code AS country_code
FROM `ghtorrent.repos_countries` a
JOIN (
    SELECT id, repo_name, path
    FROM `bigquery-public-data.github_repos.files`
    WHERE path LIKE '%.js' OR path LIKE '%.py' OR path LIKE '%.java'
) b
ON a.repo_name=b.repo_name
JOIN (
    SELECT id, content
    FROM `bigquery-public-data.github_repos.contents`
) c
ON b.id=c.id
