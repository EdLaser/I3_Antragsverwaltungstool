#!/usr/bin/python3
import pymysql

# Establish connection
connect = pymysql.connect(host='localhost', user='ruben', password='123456', database='Antraege')

with connect:
    with connect.cursor() as cursor:
        statement = "INSERT INTO universal(flag, number, title, name, mail, date , text, begzantr, vrshzverf) VALUES(0,'2021-01-01', 'Beispiel','Ruben Kraus', 'ruben@kraus.de', CURDATE(), 'Heute Testen wir den Antrag', 'Keine', 'Wir testen weiter')"
        cursor.execute(statement)

    connect.commit()