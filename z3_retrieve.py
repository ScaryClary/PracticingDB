import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

cr.execute("SELECT * FROM movies")
print(cr.fetchall())