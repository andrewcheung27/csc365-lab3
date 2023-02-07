/* Author: Andrew Cheung */
/* Email: acheun29@calpoly.edu */


CREATE TABLE Campuses(
Id INT PRIMARY KEY,
Campus VARCHAR(60),
Location VARCHAR(20),
County VARCHAR(20),
YearOpened INT,
UNIQUE(Campus, Location)
);


CREATE TABLE Disciplines(
Id INT PRIMARY KEY,
Name VARCHAR(30)
);


CREATE TABLE Degrees(
AcademicYear YEAR,
Campus INT,
Degrees INT,
PRIMARY KEY(Campus, AcademicYear),
FOREIGN KEY(Campus) REFERENCES Campuses(Id)
);


CREATE TABLE DisciplineEnrollments(
Campus INT,
Discipline INT,
AcademicYear YEAR,
Undergraduate INT,
Graduate INT,
PRIMARY KEY(Campus, AcademicYear, Discipline),
FOREIGN KEY(Campus) REFERENCES Campuses(Id),
FOREIGN KEY(Discipline) REFERENCES Disciplines(Id)
);


CREATE TABLE Enrollments(
Campus INT,
AcademicYear YEAR,
TotalEnrollment_AY INT,
FTE_AY INT,
PRIMARY KEY(Campus, AcademicYear),
FOREIGN KEY(Campus) REFERENCES Campuses(Id)
);


CREATE TABLE Faculty(
Campus INT,
AcademicYear YEAR,
Faculty DECIMAL(5, 1),
PRIMARY KEY(Campus, AcademicYear),
FOREIGN KEY(Campus) REFERENCES Campuses(Id)
);


CREATE TABLE CsuFees(
Campus INT,
AcademicYear YEAR,
CampusFee INT,
PRIMARY KEY(Campus, AcademicYear),
FOREIGN KEY(Campus) REFERENCES Campuses(Id)
);
