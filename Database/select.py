import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="employee"
)
mycursor = mydb.cursor()
mycursor.execute( "SELECT * FROM emp" )
myresult = mycursor.fetchall()

for x in myresult:
    print( x )
