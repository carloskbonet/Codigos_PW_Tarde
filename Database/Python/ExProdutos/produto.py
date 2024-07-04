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
        # Verificar todos os campos "unique". Impossibilitar a criação caso existam valores duplicados.
        productByName = findByName(_name);

        if ( productByName['status'] == 200 ):
            return { 'status' : 403 , 'message' : 'Name already registered'};


        # Criação do produto
        cursor.execute('INSERT INTO Product (name,price,quantity) VALUES (?,?,?)' , (_name, _price , _quantity));
        connection.commit();
    
        return { 'status' : 201 , 'message' : 'Product created'};

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};


# FIND
def findByName(_name:str):
    try:
        product = None;
    
        cursor.execute('SELECT * FROM Product WHERE name = ?', (_name,));
        product = cursor.fetchone();
    
        if ( product == None ):
            return { 'status' : 404 , 'message' : 'Product not found'};
        else:
            return { 'status' : 200 , 'message' : 'Product found' , 'data' : product };

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};


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
def delete(_name:str):
    try:
        productByName = findByName(_name);
    
        if ( productByName['status'] == 404 ):
            return { 'status' : 404 , 'message' : 'Product not found' };

        cursor.execute('DELETE FROM Product WHERE id = ?', (productByName['data'][0],));
        connection.commit();
    
        return { 'status' : 410 , 'message' : 'Product deleted'};
            
    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};