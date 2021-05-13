#!/usr/bin/python3
import pymysql

# Establish connection
connect = pymysql.connect(host='localhost', user='ruben', password='123456', database='Antraege')

with connect:
    with connect.cursor() as cursor:
        statement = "SELECT * FROM universal WHERE number = '2021-01-01'"
        cursor.execute(statement)
        result = cursor.fetchall()
        print(result)
    connect.commit()
