import sqlite3


def delete_movie_by_title(database_file, title):
    conn = sqlite3.connect(database_file)
    cr = conn.cursor()
    cr.execute("DELETE FROM movies WHERE title = ?;", (title,))
    conn.commit()
    cr.close()
    conn.close()
    print("Record with title '{}' deleted successfully.".format(title))


delete_movie_by_title('databaseFile.db', "The Matrix")
