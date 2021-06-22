SELECT model
FROM aircrafts JOIN seats
ON aircrafts.aircraft_code = seats.aircraft_code
GROUP BY model
HAVING COUNT(seat_no) = 
	(/* вычисляем максимальное из общего количества мест каждого самолета */
	SELECT MAX(sum_amount) AS max_sum_amount
	FROM
		(/* считаем количество мест у каждого самолета */
		SELECT aircraft_code, COUNT(seat_no) as sum_amount
		FROM seats
		GROUP BY aircraft_code
		) query_in
	);
