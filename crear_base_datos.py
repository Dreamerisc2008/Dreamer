import sqlite3

# Connect to SQLite
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create the tasks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    time TEXT NOT NULL,
    responsible TEXT NOT NULL
)
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Base de datos creada satisfactoriamente")
