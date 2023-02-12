# Author: Andrew Cheung
# Email: acheun29@calpoly.edu


import mysql.connector
from mysql.connector import Error


def execute_sql(cursor):
    # remove all records from DisciplineEnrollments except:
    # a) engineering majors (9) from CP SLO/Ponoma and Humboldt (14, 20, 8)
    # b) San Jose State (19) for disciplines with > 500 grad students
    # c) all enrollments in LA County CSUs where grad > undergrad enrollment
    # (campus id = 4, 9, 10, 13, 14)
    cursor.execute("DELETE FROM DisciplineEnrollments WHERE NOT (Discipline = 9 AND Campus IN(8, 14, 20)) AND NOT (Campus = 19 AND Graduate > 500) AND NOT (Campus IN(4, 9, 10, 13, 14) AND Graduate > Undergraduate);")

    # output contents of DisciplineEnrollments
    cursor.execute("SELECT * FROM DisciplineEnrollments ORDER BY Campus, Discipline;")
    records = cursor.fetchall()
    print("------------------------------------------------------------------")
    for r in records:
        print(r)
    print("------------------------------------------------------------------")

    # from CsuFees, keep records matching all the following conditions:
    # a) fee > $2,500
    # b) the year is 2002 or 2004-2006
    # c) campus is CP SLO/Ponoma or San Diego State (14, 20, 17)
    cursor.execute("DELETE FROM CsuFees WHERE NOT (CampusFee > 2500) OR NOT (AcademicYear IN(2002, 2004, 2005, 2006)) OR NOT (Campus IN(14, 17, 20));")

    # output contents of CsuFees
    cursor.execute("SELECT * FROM CsuFees ORDER BY Campus, AcademicYear;")
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
