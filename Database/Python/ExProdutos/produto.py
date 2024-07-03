# Back-end

import sqlite3;

connection = sqlite3.connect('store.db');
cursor = connection.cursor();

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        id INTEGER PRIMARY KEY,
        name    VARCHAR(36) UNIQUE NOT NULL,
        price   FLOAT NOT NULL,
        quantity    INTEGER NOT NULL
    );
''');

# CREATE
def create(_name:str , _price:float , _quantity:int):
    try:
        # Criação do produto
        cursor.execute('INSERT INTO Product (name,price,quantity) VALUES (?,?,?)' , (_name, _price , _quantity));
        connection.commit();
    
        return { 'status' : 201 , 'message' : 'Product created'};

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};


# FIND
def findByName():
    pass;


# SELECT
def select():
    try:
        products = [];

        cursor.execute('SELECT * FROM Product');
        products = cursor.fetchall();
    
        return { 'status' : 200 , 'message' : 'Select Products' , 'data': products };

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};


# UPDATE


# DELETE
def delete():
    pass;