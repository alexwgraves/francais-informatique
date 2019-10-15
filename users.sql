-- find the percentage of users in the table who have their country code set
SELECT SUM(country_code!='\\N')/COUNT(*) FROM users; -- 0.0758 = 7.58%
-- number of users who have their country code set
SELECT SUM(country_code!='\\N') FROM users; -- 2405811

-- get logins of France users from GHTorrent database
SELECT login FROM users WHERE country_code='fr';
-- find the percentage of users with country codes who have theirs set to France
SELECT SUM(country_code='fr')/SUM(country_code!='\\N') FROM users; -- 0.0299 = 2.99%
-- number of users who have their country code set to France
SELECT SUM(country_code='fr') FROM users; -- 71852

-- get logins of Switzerland users from GHTorrent database
SELECT login FROM users WHERE country_code='ch';
-- find the percentage of users with country codes who have theirs set to Switzerland
SELECT SUM(country_code='ch')/SUM(country_code!='\\N') FROM users; -- 0.0077 = 0.77%
-- number of users who have their country code set to Switzerland
SELECT SUM(country_code='ch') FROM users; -- 18553

-- get logins of Belgium users from GHTorrent database
SELECT login FROM users WHERE country_code='be';
-- find the percentage of users with country codes who have theirs set to Belgium
SELECT SUM(country_code='be')/SUM(country_code!='\\N') FROM users; -- 0.0061 = 0.61%
-- number of users who have their country code set to Belgium
SELECT SUM(country_code='be') FROM users; -- 14630

-- get logins of Quebec users from GHTorrent database
SELECT login from users where country_code='ca' and state='Quebec';
-- find the percentage of users with country codes who have theirs set to Quebec
SELECT SUM(country_code='ca' and state='Quebec')/SUM(country_code!='\\N' and state!='\\N') FROM users; -- 0.0002 = 0.02%
-- number of users who have their country code set to Quebec
SELECT SUM(country_code='ca' and state='Quebec') FROM users; -- 494

-- get logins of Senegal users from GHTorrent database
SELECT login FROM users WHERE country_code='sn';
-- find the percentage of users with country codes who have theirs set to Senegal
SELECT SUM(country_code='sn')/SUM(country_code!='\\N') FROM users; -- 0.0001 = 0.01%
-- number of users who have their country code set to Senegal
SELECT SUM(country_code='sn') FROM users; -- 354
