# Author: Andrew Cheung
# Email: acheun29@calpoly.edu


import mysql.connector
from mysql.connector import Error


def execute_sql(cursor):
    # remove goods that are cheaper than $5
    # since the Items table references Goods, must add ON DELETE CASCADE first
    cursor.execute("ALTER TABLE Items DROP FOREIGN KEY fk_items_2;")
    cursor.execute("ALTER TABLE Items ADD CONSTRAINT fk_items_2 FOREIGN KEY(Item) REFERENCES Goods(Id) ON DELETE CASCADE;")
    cursor.execute("DELETE FROM Goods WHERE Price < 5.00;")

    # increase the price of chocolate-flavored goods by 20%
    cursor.execute("UPDATE Goods SET Price = Price * 1.20 WHERE Flavor = 'Chocolate';")

    # reduce the price of lemon-flavored goods by $2
    cursor.execute("UPDATE Goods SET Price = Price - 2.00 WHERE Flavor = 'Lemon';")

    # reduce the price of all other cakes (not chocolate or lemon) by 10%
    cursor.execute("UPDATE Goods SET Price = Price * 0.90 WHERE Food = 'Cake' AND NOT Flavor = 'Chocolate' AND NOT Flavor = 'Lemon';")

    # make the price of all pies equal to the cheapest cake
    # (lemon cake $6.95 because of previous changes)
    cursor.execute("UPDATE Goods SET Price = 6.95 WHERE Food = 'Pie';")

    # output contents
    cursor.execute("SELECT * FROM Goods ORDER BY Id;")
    records = cursor.fetchall()
    print("------------------------------------------------------------------")
    for r in records:
        print(r)
    print("------------------------------------------------------------------")


def main():
    pwdFilename = "../account.info"
    try:
        pwdFile = open(pwdFilename, "r")
        userName = pwdFile.readline().strip()
        dbName = userName
        passString = pwdFile.readline().strip()
    except FileNotFoundError as e:
        print(e)
        return 1

    hostName = "mysql.labthreesixfive.com"
    portName = "3306"

    connector = None
    cursor = None
    try:
        connector = mysql.connector.connect(host=hostName, port=portName,
                                            database=dbName, user=userName,
                                            password=passString)
        cursor = connector.cursor()
        execute_sql(cursor)

    except Error as e:
        print("connection error:", e)

    finally:
        if connector is not None and connector.is_connected():
            if cursor is not None:
                cursor.close()
            connector.close()
            print("done")


if __name__ == "__main__":
    main()
