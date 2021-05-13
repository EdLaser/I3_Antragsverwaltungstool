#!/usr/bin/python3
import pymysql
import sys

# Establish connection
connect = pymysql.connect(host='localhost', user='ruben', password='123456', database='Antraege')
# Set the passed values
# values = "0" + sys.argv[1] + "," + sys.argv[2] + sys.argv[3] + sys.argv[4] + sys.argv[5] + sys.argv[6] + sys.argv[7] + sys.argv[8]
cursor = connect.cursor()
#statement = "INSERT INTO advisory_member(flag, number, title, fname, lname, mail, date , text, frg1, frg2, frg3, frg4) VALUES(0, " \
#           "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
# Try executing
with connect:
    with connect.cursor() as cursor:
        statement = "INSERT INTO advisory_member(flag, number, title, fname, lname, mail, date , text, frg1, frg2, frg3,frg4) VALUES(0,'2021-01-01', 'Beispiel','Ruben', 'Kraus', 'ruben@kraus.de', CURDATE(), 'Heute Testen wir den Antrag', 'Keine', 'Ganz viel Zeit', 'Wenig Zeit', 'Ich knalle alle ab')"
        cursor.execute(statement)

    connect.commit()
