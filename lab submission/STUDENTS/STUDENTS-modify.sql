/* Author: Andrew Cheung */
/* Email: acheun29@calpoly.edu */


-- create a GPA column in the students table
ALTER TABLE List
ADD COLUMN(GPA DECIMAL(3, 2))


-- delete students who aren't in grades 0 or 1
DELETE FROM List
WHERE Grade = 0 OR Grade = 1;


-- add the teacher ERNESTO VALDEZ in classroom 115
INSERT INTO Teachers(FirstName, LastName, Classroom)
VALUES('ERNESTO', 'VALDEZ', 115);


-- move SHERMAN DROP, THEO HUTCHENS, and FRANKLYN BRINE to classroom 120
UPDATE List
SET Classroom = 120
WHERE (FirstName = 'SHERMAN' AND LastName = 'DROP')
    OR (FirstName = 'THEO' AND LastName = 'HUTCHENS')
    OR (FirstName = 'FRANKLYN' AND LastName = 'BRINE');


-- set the GPA of all first graders to 3.25
UPDATE List
SET GPA = 3.25
WHERE Grade = 1;


-- set the GPA of kindergarten students in room 105 to 2.9
UPDATE List
SET GPA = 2.9
WHERE GRADE = 0 AND Classroom = 105;


-- set the GPA of kindergarten students in room 106 to 3.5
UPDATE List
SET GPA = 3.5
WHERE Grade = 0 AND Classroom = 106;


-- add kindergarteners YORAM LEVY, JUSTIN WASHINGTON, and ASTRID NG
-- to room 115 with GPA 3.2
INSERT INTO List(FirstName, LastName, Grade, Classroom, GPA)
VALUES('YORAM', 'LEVY', 0, 115, 3.2);
INSERT INTO List(FirstName, LastName, Grade, Classroom, GPA)
VALUES('JUSTIN', 'WASHINGTON', 0, 115, 3.2);
INSERT INTO List(FirstName, LastName, Grade, Classroom, GPA)
VALUES('ASTRID', 'NG', 0, 115, 3.2);


-- set the GPA of COLLIN VANVLIET to 4.0
UPDATE List
SET GPA = 4.0
WHERE FirstName = 'COLLIN' AND LastName = 'VANVLIET';


-- set the GPA of KITTIE MOWAT to be 0.3 higher
UPDATE List
SET GPA = GPA + 0.3
WHERE FirstName = 'KITTIE' AND LastName = 'MOWAT';


-- set the GPAs of SHERON NAKAHARA and BENNIE BYRUM to be 10% higher
UPDATE List
SET GPA = GPA * 1.10
WHERE (FirstName = 'SHERON' AND LastName = 'NAKAHARA')
    OR (FirstName = 'BENNIE' AND LastName = 'BYRUM');


-- output the students table sorted by GPA, Grade, then LastName,
-- and output the teachers table
SELECT * FROM List
ORDER BY GPA, Grade, LastName;
SELECT * FROM Teachers;
