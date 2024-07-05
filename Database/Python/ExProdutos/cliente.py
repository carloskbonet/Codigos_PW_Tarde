# Back-end

import sqlite3;

connection = sqlite3.connect('store.db');
cursor = connection.cursor();

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer (
        id INTEGER PRIMARY KEY,
        name VARCHAR(64) NOT NULL,
        cpf VARCHAR(18) UNIQUE NOT NULL,
        email VARCHAR(64) UNIQUE NOT NULL,
        phone   VARCHAR(18)
    );
'''
);