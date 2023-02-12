# Author: Andrew Cheung
# Email: acheun29@calpoly.edu


import mysql.connector
from mysql.connector import Error


def execute_sql(cursor):
    # remove all flights except the ones to/from AKI
    cursor.execute("DELETE FROM Flights WHERE !(SourceAirport = 'AKI') AND !(DestAirport = 'AKI');")

    # for flights not operated by Continental, Virgin, or AirTran, increase the
    # flight number by 2000.
    # airline numbers: Continental = 7, Virgin = 12, AirTran = 10
    cursor.execute("UPDATE Flights SET FlightNo = FlightNo + 2000 WHERE Airline = 7 OR Airline = 12 OR Airline = 10;")

    # for pairs of flights to/from AKI that aren't operated by Continental,
    # FlightNo += 1 if even, FlightNo -= 1 if odd.
    # do even += 2001, odd -= 1, even -= 2000 so there are no duplicates
    cursor.execute("UPDATE Flights SET FlightNo = FlightNo + 2001 WHERE Airline = 7 AND MOD(FlightNo, 2) = 0;")
    cursor.execute("UPDATE Flights SET FlightNo = FlightNo - 1 WHERE Airline = 7 AND MOD(FlightNo, 2) = 1;")
    cursor.execute("UPDATE Flights SET FlightNo = FlightNo - 2000 WHERE Airline = 7 AND MOD(FlightNo, 2) = 0;")

    # set airline to Continental for all flights to/from AKI,
    # except Virgin and AirTran
    cursor.execute("UPDATE Flights SET Airline = 7 WHERE Airline != 12 AND Airline != 10;")

    # output contents
    cursor.execute("SELECT * FROM Flights ORDER BY Airline, FlightNo;")
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
