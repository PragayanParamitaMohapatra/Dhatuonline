import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="employee"
)
mycursor = mydb.cursor()
mycursor.execute( "CREATE TABLE emp (name varchar(255),address varchar(255))" )
