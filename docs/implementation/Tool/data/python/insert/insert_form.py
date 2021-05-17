import pymysql
import sys

# Establish connection
database = pymysql.connect('localhost', 'ruben', '123456', 'Antraege')
# Set the passed values
# values = "0" + sys.argv[1] + "," + sys.argv[2] + sys.argv[3] + sys.argv[4] + sys.argv[5] + sys.argv[6] + sys.argv[7] + sys.argv[8]
cursor = database.cursor()
statement = "INSERT INTO antrag(status, nummer, titel, vorname, name, mail, datum, text, grund, vorgehen) VALUES(0, " \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s ) "

# Try executing
try:
    # Execute the cursor
    cursor.execute(statement, (sys.argv[1], sys.argv[2], sys.argv[3],
                               sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]))
    database.commit()
except:
    # Rollback if failed
    database.rollback()
finally:
    database.close()