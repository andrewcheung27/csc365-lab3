/* Author: Andrew Cheung */
/* Email: acheun29@calpoly.edu */


CREATE TABLE Continents(
ContId INT PRIMARY KEY,
Continent VARCHAR(20),
CONSTRAINT uniq_continents_1 UNIQUE(Continent)
);


CREATE TABLE Countries(
CountryId INT PRIMARY KEY,
CountryName VARCHAR(20),
Continent INT,
CONSTRAINT fk_countries_1 FOREIGN KEY(Continent) REFERENCES Continents(ContId),
CONSTRAINT uniq_countries_1 UNIQUE(CountryName, Continent)
);


CREATE TABLE CarMakers(
Id INT PRIMARY KEY,
Maker VARCHAR(20),
FullName VARCHAR(30),
Country INT,
CONSTRAINT fk_carmakers_1 FOREIGN KEY(Country) REFERENCES Countries(CountryId)
);


CREATE TABLE ModelList(
ModelId INT PRIMARY KEY,
Maker INT,
Model VARCHAR(20),
CONSTRAINT fk_modellist_1 FOREIGN KEY(Maker) REFERENCES CarMakers(Id),
CONSTRAINT uniq_modellist_1 UNIQUE(Model)
);


CREATE TABLE CarNames(
Id INT PRIMARY KEY,
Model VARCHAR(20),
Make VARCHAR(40),
CONSTRAINT fk_carnames_1 FOREIGN KEY(Model) REFERENCES ModelList(Model)
);


CREATE TABLE CarsData(
Id INT PRIMARY KEY,
MPG INT,
Cylinders INT,
Edispl INT,
Horsepower INT,
Weight INT,
Accelerate DECIMAL(4, 1),
CarYear YEAR,
CONSTRAINT fk_carsdata_1 FOREIGN KEY(Id) REFERENCES CarNames(Id)
);
