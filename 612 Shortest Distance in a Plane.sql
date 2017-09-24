/*
Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.

Write a query to find the shortest distance between these points rounded to 2 decimals.
| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:
| shortest |
|----------|
| 1.00     |
Note: The longest distance among all the points are less than 10000.
*/
SELECT
    distance AS shortest
FROM 
    (SELECT
        ROUND(SQRT( POWER(a.x - b.x, 2) + POWER(a.y - b.y, 2) ),2) AS distance
    FROM point_2d a
    CROSS JOIN point_2d b
    WHERE a.x != b.x OR a.y != b.y
    ) d
ORDER BY distance
LIMIT 1