-- List all records with a score >= 10 in the table 
-- second_table of the db hbtn_0c_0 on MySQL server.

SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
