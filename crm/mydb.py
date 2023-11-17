import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Data0rb1$',
     auth_plugin='mysql_native_password'
)

#CURSOR OBJECT
cursorObject = dataBase.cursor()

#CREATING A DB
cursorObject.execute("CREATE DATABASE crmio")

print("All Good!")