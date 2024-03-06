import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

#uses the database file specified with cr
#pulls the list of all the tables in that databse
cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cr.fetchall()
print (tables)

#i found out the table name is movies
#this will pull all the columns from that table
cr.execute("PRAGMA table_info({});".format("movies"))
columns = cr.fetchall()
column_names = [column[1] for column in columns]
print (column_names)

#pulls data from table "movies"
cr.execute("SELECT * FROM movies")
print(cr.fetchall())