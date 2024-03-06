import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

#uses the database file specified with cr
#pulls the list of all the tables in that databse
cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cr.fetchall()
print (tables)

#pulls data from table "movies"
cr.execute("SELECT * FROM movies")
print(cr.fetchall())