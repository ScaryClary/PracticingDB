import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

def add_movie(title, director, year, genre):
    cr.execute("""
        INSERT INTO movies (title, director, year, genre) 
        VALUES (?,?,?,?)""",(title,director,year,genre)
        )
    conn.commit()
    print("Movie added :)")

add_movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
add_movie("The Godfather", "Francis Ford Coppola", 1972, "Crime")
add_movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama")
add_movie("Pulp Fiction", "Quentin Tarantino", 1994, "Crime")
add_movie("The Dark Knight", "Christopher Nolan", 2008, "Action")
add_movie("Schindler\'s List", "Steven Spielberg", 1993, "Biography")
add_movie("The Lord of the Rings: The Return of the King", "Peter Jackson", 2003, "Fantasy")
add_movie("Fight Club", "David Fincher", 1999, "Drama")
add_movie("Forrest Gump", "Robert Zemeckis", 1994, "Romance")
add_movie("The Matrix", "The Wachowskis", 1999, "Action")