#!/usr/bin/python3
import pymysql

# Establish connection
connect = pymysql.connect(host='localhost', user='ruben', password='123456', database='Antraege')

with connect:
    with connect.cursor() as cursor:
        statement = "INSERT INTO finance(flag, number, title, name, mail, date , text, begzantr, haushplan, vrshzverf) VALUES(0,'2021-01-01', 'Beispiel','Ruben Kraus', 'ruben@kraus.de', CURDATE(), 'Ich brauche Geld für Bier', 'Will halt Bier saufen', 'Biergeld', 'Gebt mir die Kohle')"
        cursor.execute(statement)

    connect.commit()