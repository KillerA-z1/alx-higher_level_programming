-- a script that lists number of records with same score in second_table of the database hbtn_0c_0.
SELECT `score`, COUNT('score') AS number
FROM second_table GROUP BY `score`
ORDER BY `score` DESC;