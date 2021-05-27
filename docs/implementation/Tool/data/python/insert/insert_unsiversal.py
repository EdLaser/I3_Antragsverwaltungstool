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
reason = values.getvalue('begzantr')
suggestion = values.getvalue('vrshzverf')

with connect:
    with connect.cursor() as cursor:
        statement = "INSERT INTO universal(flag, number, date, title, name, mail, text, reason, suggestion) VALUES(" \
                    "0,'2021-01-01', CURDATE(), 'Beispiel','Ruben Kraus', 'ruben@kraus.de', 'Heute Testen wir den " \
                    "Antrag', 'Keine', 'Wir testen weiter') "
        cursor.execute(statement)

    connect.commit()
