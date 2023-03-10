/* Author: Andrew Cheung */
/* Email: acheun29@calpoly.edu */


CREATE TABLE Teachers(
LastName VARCHAR(20),
FirstName VARCHAR(20),
Classroom INT PRIMARY KEY,
CONSTRAINT uniq_teachers_1 UNIQUE(FirstName, LastName)
);


CREATE TABLE List(
LastName VARCHAR(20),
FirstName VARCHAR(20),
Grade INT,
Classroom INT,
PRIMARY KEY(LastName, FirstName, Classroom),
CONSTRAINT fk_list_1 FOREIGN KEY(Classroom) REFERENCES Teachers(Classroom)
);
