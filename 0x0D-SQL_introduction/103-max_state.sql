-- script to display max temp of state

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
