#ismaeel bashir

#creating project database

#imports the mysql library
import mysql.connector

#creates an instance of a connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    charset = "utf8"
    )

#creates a variable for a cursor
mycursor = mydb.cursor()

#creates a table for the player
mycursor.execute("CREATE DATABASE Bushi")

#commits and closes the database connection
mycursor.close()
mydb.close()


#creates an instance of a connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    charset = "utf8",
    database = "Bushi" 
    )

#creates a variable for a cursor
mycursor = mydb.cursor()

#creates a table for the player
mycursor.execute("CREATE TABLE player (earthunlock TINYINT, waterunlock TINYINT, fireunlock TINYINT, earthfinish TINYINT, waterfinish TINYINT, firefinish TINYINT, corruptfinish TINYINT, save INT(10) PRIMARY KEY, active TINYINT)")

#inserts row 1
mycursor.execute("INSERT INTO player (earthunlock,waterunlock,fireunlock,earthfinish,waterfinish,firefinish,corruptfinish,save,active) VALUES (0,0,0,0,0,0,0,1,0)")

#commits and closes the database connection
mydb.commit()

#inserts row 2
mycursor.execute("INSERT INTO player (earthunlock,waterunlock,fireunlock,earthfinish,waterfinish,firefinish,corruptfinish,save,active) VALUES (0,0,0,0,0,0,0,2,0)")

#commits and closes the database connection
mydb.commit()

#inserts row 2
mycursor.execute("INSERT INTO player (earthunlock,waterunlock,fireunlock,earthfinish,waterfinish,firefinish,corruptfinish,save,active) VALUES (0,0,0,0,0,0,0,3,0)")

#commits and closes the database connection
mydb.commit()

mycursor.close()
mydb.close()
