import sqlite3

connection = sqlite3.connect("rpg_db.sqlite3")
cursor = connection.cursor()
query = 'SELECT * FROM charactercreator_character;'
cursor.execute(query)
results = cursor.fetchall()
results[:5]
