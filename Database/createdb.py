import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="employee"
)
mycursor = mydb.cursor()
# db1=mycursor.execute("CREATE DATABASE employee")
# print("Database is created successfully")
mycursor.execute( "CREATE TABLE emp(id INT_AUTOINCREMENT_PRIMARYKEY,name varchar(255),phonenum number(10) " )

# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)
