import sqlite3

conn = sqlite3.connect('webhooks.db')
c = conn.cursor()

c.execute('SELECT * FROM transactions;')
print c.fetchone()
conn.close()
