# Author: Andrew Cheung
# Email: acheun29@calpoly.edu
import mysql.connector
from mysql.connector import Error


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
        cursor.execute("SELECT * FROM Airlines")
        records = cursor.fetchall()
        print("----------------------------------------------------")
        for r in records:
            print(r)
        print("----------------------------------------------------")

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
