SELECT
	t1.airport_name,
	t2.airport_name,
	ROUND(point(t1.coordinates) <@> point(t2.coordinates)) as distance
FROM 
	airports t1 JOIN airports t2
ON t1.airport_name<>t2.airport_name	
ORDER BY distance DESC
FETCH FIRST 1 ROW ONLY