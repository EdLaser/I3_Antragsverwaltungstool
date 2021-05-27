#!/usr/bin/python3
import pymysql

# Establish connection
connect = pymysql.connect(host='192.168.19.129', user='ruben', password='1234', database='Antraege')

with connect:
    with connect.cursor() as cursor:
        statement = "SELECT * FROM finance WHERE number = '2021-01-01'"
        cursor.execute(statement)
        result = cursor.fetchall()
        print(result)
