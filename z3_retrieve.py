import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

#uses the database file specified with cr
#pulls the list of all the tables in that databse
cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cr.fetchall()
print ("list of tables in the DB file:\n",tables,"\n")

#i found out the table name is movies
#this will pull all the columns from that table
cr.execute("PRAGMA table_info({});".format("movies"))
columns = cr.fetchall()
column_names = [column[1] for column in columns]
print ("list of columns in the movie table:\n",column_names,"\n")

#pulls data from table "movies"
cr.execute("SELECT * FROM movies")
print("list of data in the movies table:\n",cr.fetchall(),"\n")

#pulls specific data
cr.execute("SELECT title, director, year FROM movies WHERE year = ?;", (2010,))
moviesFrom2010 = cr.fetchall()
print ("movies from 2010:\n",moviesFrom2010)