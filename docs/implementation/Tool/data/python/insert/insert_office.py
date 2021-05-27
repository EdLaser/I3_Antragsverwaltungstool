#!/usr/bin/python3
import cgi
import pymysql

# Establish connection
connect = pymysql.connect(host='192.168.19.129', user='ruben', password='1234', database='Antraege')

# get cgi values
values = cgi.FieldStorage()
number = "2021-01-01"
title = values.getvalue('title')
office = values.getvalue('election_input')
name = values.getvalue('name')
mail = values.getvalue('mail')
text = values.getvalue('antrtext')
frg1 = values.getvalue('frg1')
frg2 = values.getvalue('frg2')
frg3 = values.getvalue('frg3')
frg4 = values.getvalue('frg4')
frg_spez_1 = values.getvalue('frg5')
frg_spez_2 = values.getvalue('frg6')
frg_spez_3 = values.getvalue('frg7')

with connect:
    with connect.cursor() as cursor:
        statement = "INSERT INTO position(flag, number, date, title, name, mail , text, frg1, frg2, frg3, frg4, " \
                    "frg_spez_1, frg_spez_2, frg_spez_3) VALUES(0,'2021-01-01', CURDATE(), 'Beispiel','Ruben Kraus', " \
                    "'ruben@kraus.de', 'Heute Testen wir den Antrag', 'Keine', 'Ganz viel Zeit', " \
                    "'Wenig Zeit', 'Ich knalle alle ab', 'Test', 'Test', 'Test') "
        cursor.execute(statement)
    connect.commit()
