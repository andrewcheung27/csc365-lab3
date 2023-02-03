/* Author: Andrew Cheung */
/* Email: acheun29@calpoly.edu */


-- delete tuples from CarsData which don't satisfy any of the conditions
DELETE FROM CarsData
WHERE !((CarYear = '1978' OR CarYear = '1979') AND MPG >= 20)
    AND !(MPG >= 26 AND Horsepower >= 110)
    AND !(Cylinders = 8 AND Accelerate < 10);


-- output the car data table, sorted by year and then car id
SELECT * FROM CarsData
ORDER BY CarYear, Id;


-- remove all columns from CarsData except car id, car year, acceleration,
-- MPG, and number of cylinders
ALTER TABLE CarsData
DROP Edispl, Horsepower, Weight;


-- remove all tuples from CarsData with <= 5 cylinders
DELETE FROM CarsData
WHERE Cylinders <= 5;


-- output the car data table again
SELECT * FROM CarsData
ORDER BY CarYear, Id;
