import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='tshego7538'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mydatabase")

print("All done!")
