#!/usr/bin/python3
import pymysql

# Establish connection
connect = pymysql.connect(host='localhost', user='root', password='123456', database='Antraege')

with connect:
    with connect.cursor() as cursor:
        statement = "INSERT INTO advisory_member(flag, number, title, fname, lname, mail, date , text, frg1, frg2, frg3,frg4) VALUES(0,'2021-01-01', 'Beispiel','Ruben', 'Kraus', 'ruben@kraus.de', CURDATE(), 'Heute Testen wir den Antrag', 'Keine', 'Ganz viel Zeit', 'Wenig Zeit', 'Ich knalle alle ab')"
