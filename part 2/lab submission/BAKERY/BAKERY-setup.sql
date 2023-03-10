/* Author: Andrew Cheung */
/* Email: acheun29@calpoly.edu */


CREATE TABLE Goods(
Id VARCHAR(20) PRIMARY KEY,
Flavor VARCHAR(20),
Food VARCHAR(20),
Price DECIMAL(5, 2),
CONSTRAINT uniq_goods_1 UNIQUE(Flavor, Food)
);


CREATE TABLE Customers(
Id INT PRIMARY KEY,
LastName VARCHAR(20),
FirstName VARCHAR(20)
);


CREATE TABLE Receipts(
ReceiptNumber INT PRIMARY KEY,
ReceiptDate DATE,
CustomerId INT,
CONSTRAINT fk_receipts_1 FOREIGN KEY(CustomerId) REFERENCES Customers(Id)
);


CREATE TABLE Items(
Receipt INT,
Ordinal INT,
Item VARCHAR(20),
PRIMARY KEY(Receipt, Ordinal),
CONSTRAINT fk_items_1 FOREIGN KEY(Receipt) REFERENCES Receipts(ReceiptNumber),
CONSTRAINT fk_items_2 FOREIGN KEY(Item) REFERENCES Goods(Id)
);
