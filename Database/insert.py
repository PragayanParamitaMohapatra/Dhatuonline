import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="employee"
)
mycursor = mydb.cursor()
sql = "insert into emp (name,address) values(%s,%s)"
val = [("guddi", "bnj"), ("punu", "bam"), ("suru", "bbsr")]
mycursor.executemany( sql, val )
mydb.commit()
print( mycursor.rowcount, "record inserted." )
