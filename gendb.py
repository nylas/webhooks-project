import sqlite3

conn = sqlite3.connect('webhooks.db')
c = conn.cursor()
c.execute("""CREATE TABLE transactions (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        public_id VARCHAR(64), type VARCHAR(32), record_id INTEGER);""")

conn.commit()
conn.close()
