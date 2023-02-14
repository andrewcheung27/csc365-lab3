# Author: Andrew Cheung
# Email: acheun29@calpoly.edu


import mysql.connector
from mysql.connector import Error


def execute_sql(cursor):
    # replace 'bass balalaika' with 'awesome bass balalaika'
    # and 'guitar' with 'acoustic guitar'.
    # first, increase Instruments.Instrument attribute to VARCHAR(30)
    cursor.execute("ALTER TABLE Instruments MODIFY Instrument VARCHAR(30);")
    cursor.execute("UPDATE Instruments SET Instrument = 'awesome bass balalaika' WHERE Instrument = 'bass balalaika';")
    cursor.execute("UPDATE Instruments SET Instrument = 'guitar' WHERE Instrument = 'acoustic guitar';")

    # remove all records from Instruments except info about
    # 'awesome bass balalaika' or Anne-Marit (3)
    cursor.execute("DELETE FROM Instruments WHERE NOT Instrument = 'awesome bass balalaika' AND NOT BandmateId = 3;")


    # output contents of Instruments
    cursor.execute("SELECT * FROM Instruments ORDER BY SongId, BandmateId;")
    records = cursor.fetchall()
    print("------------------------------------------------------------------")
    for r in records:
        print(r)
    print("------------------------------------------------------------------")

    # add a NumSongs attribute to the Albums table
    cursor.execute("ALTER TABLE Albums ADD COLUMN(NumSongs INT);")

    # update the number of songs for each album
    cursor.execute("UPDATE Albums SET NumSongs = 13 WHERE AId = 1;")
    cursor.execute("UPDATE Albums SET NumSongs = 12 WHERE AId = 2;")
    cursor.execute("UPDATE Albums SET NumSongs = 19 WHERE AId = 3;")
    cursor.execute("UPDATE Albums SET NumSongs = 11 WHERE AId = 4;")

    # output contents of Albums
    cursor.execute("SELECT * FROM Albums ORDER BY YearReleased;")
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
