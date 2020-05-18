import sqlite3

db = "corrupt.sqlite"
conn = sqlite3.connect(db)
d_cook = conn.cursor()
donn = sqlite3.connect('chinook.sqlite')
cook = donn.cursor()


def delete_track(title):
    DELETE FROM cook
    WHERE conn IS NULL;
    
    SELECT * FROM cook;
