import sqlite3


conn = sqlite3.connect('journal.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, title TEXT, content TEXT)')
conn.commit()
conn.close()
