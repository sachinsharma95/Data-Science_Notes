import mysql.connector

mydb  = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

mycursor = mydb.cursor()
print(mydb)

# mycursor.execute("CREATE DATABASE if not exists test2")
# mycursor.execute("CREATE TABLE if not exists  test2.test_table(c1 INT , c2 VARCHAR(50) )")
mycursor.execute("INSERT INTO test2.test_table values(12,'sachin')")
mycursor.execute("INSERT INTO test2.test_table values(13,'sachin1')")
mycursor.execute("INSERT INTO test2.test_table values(14,'sachin2')")
mycursor.execute("INSERT INTO test2.test_table values(15,'sachin3')")

mycursor.execute("select * from test2.test_table")
# mydb.close()

for i in mycursor.fetchall():
    print(i)
