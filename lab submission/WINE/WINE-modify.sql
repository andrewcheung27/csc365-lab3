/* Author: Andrew Cheung */
/* Email: acheun29@calpoly.edu */


-- remove Appellation and Name columns
ALTER TABLE Wine
DROP Appellation, Name;


-- drop all tuples except Zinfandels with a score >= 92
DELETE FROM Wine
WHERE !(Appellation = 'Zinfandel' AND Score >= 92);


-- add a column called Revenue
ALTER TABLE Wine
ADD COLUMN(Revenue INT AFTER Price);


-- for all tuples in the table, set revenue to price * cases
UPDATE Wine
SET Revenue = Price * Cases;


-- output the tables, sorted by revenue
SELECT * FROM Wine
ORDER BY Revenue;
