#!/usr/bin/python3
import pymysql
import cgi

# Establish connection
connect = pymysql.connect(host='localhost', user='ruben', password='123456', database='Antraege')

# get cgi values
values = cgi.FieldStorage()
number = "2021-01-01"
title = "Testantrag .py"
name = "Ruben Kraus"
mail = values.getvalue('')
# date =
text = values.getvalue('antrtext')
frg1 = values.getvalue('frg1')
frg2 = values.getvalue('frg2')
frg3 = values.getvalue('frg3')
frg4 = values.getvalue('frg4')

# Test VALUES(0,'2021-01-01', 'Beispiel','Ruben Kraus', 'ruben@kraus.de', CURDATE(), 'Heute Testen wir den Antrag', 'Keine', 'Ganz viel Zeit', 'Wenig Zeit', 'Ich knalle alle ab')

# Try executing
with connect:
    with connect.cursor() as cursor:
        statement = "INSERT INTO advisory_member(flag, number, title, name, mail, date , text, frg1, frg2, frg3,frg4) VALUES(0, %s, %s, %s, %s, CURDATE(), %s, %s, %s, %s, %s)"
        cursor.execute(statement, (number, title, name, mail, text, frg1, frg2, frg3, frg4))

    connect.commit()
