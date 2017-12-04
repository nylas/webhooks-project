import uuid
import random
import sqlite3

conn = sqlite3.connect('webhooks.db')
c = conn.cursor()

inserts = []
for i in range(100):
    public_id = str(uuid.uuid1())
    type = random.choice(['create', 'update', 'delete'])
    record_id = random.randrange(1, 100000)
    inserts.append([public_id, type, record_id])

print inserts
c.executemany('''INSERT INTO transactions (public_id, type, record_id) VALUES (?, ?, ?)''', inserts);

conn.commit()
conn.close()
