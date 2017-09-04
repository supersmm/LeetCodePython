/*
A pupil Tim gets homework to identify whether three line segments could possibly form a triangle.

However, this assignment is very heavy because there are hundreds of records to calculate.
Could you help Tim by writing a query to judge whether these three sides can form a triangle, assuming table triangle holds the length of the three sides x, y and z.
| x  | y  | z  |
|----|----|----|
| 13 | 15 | 30 |
| 10 | 20 | 15 |
For the sample data above, your query should return the follow result:
| x  | y  | z  | triangle |
|----|----|----|----------|
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |

In Math, three segments can form a triangle only if the sum of any of the two segments is larger than the third one. (In other words, the subtraction of any of the two segments are smaller than the third one.)
*/
SELECT 
    *,
    CASE WHEN x+y>z AND x+z>y AND y+z>x THEN 'Yes'
    ELSE 'No' END    AS triangle
FROM triangle;