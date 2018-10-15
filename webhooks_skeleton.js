const sqlite3 = require('sqlite3')

let db = new sqlite3.Database('webhooks.db');
let sqlQuery = 'SELECT * FROM transactions';

db.all(sqlQuery, [], (err, rows) => {
  console.log(rows[0]);
});

db.close();
