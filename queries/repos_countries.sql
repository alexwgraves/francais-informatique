-- gets data for the month of April 2019
SELECT repo.name, country_code
FROM [githubarchive:month.201904] a
JOIN (
  SELECT login, country_code
  FROM [ghtorrent.users]
) b
ON a.actor.login=b.login
WHERE type = 'PushEvent'
GROUP BY repo.name, country_code
