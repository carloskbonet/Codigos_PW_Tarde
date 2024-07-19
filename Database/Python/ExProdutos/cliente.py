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


# CREATE
def create(_name:str, _cpf:str, _email:str , _phone:str):
    try:
        # Verificar todos os campos "unique". Impossibilitar a criação caso existam valores duplicados.
        customerByCPF = findByCPF(_cpf);

        if ( customerByCPF['status'] == 200 ):
            return { 'status' : 403 , 'message' : 'CPF already registered'};

        customerByEmail = findByEmail(_email);

        if ( customerByEmail['status'] == 200 ):
            return { 'status' : 403 , 'message' : 'Email already registered'};

        # Criação do cliente
        cursor.execute('INSERT INTO Customer (name, cpf , email, phone) VALUES (?,?,?,?)' , (_name,_cpf,_email,_phone));
        connection.commit();
    
        return { 'status' : 201 , 'message' : 'Customer created'};

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};


# Read - FIND
def findByCPF(_cpf:str):
    try:
        customer = None;
    
        cursor.execute('SELECT * FROM Customer WHERE cpf = ?', (_cpf,));
        customer = cursor.fetchone();
    
        if ( customer == None ):
            return { 'status' : 404 , 'message' : 'Customer not found'};
        else:
            return { 'status' : 200 , 'message' : 'Customer found' , 'data' : customer };

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};

# Read - FIND
def findByEmail(_email:str):
    try:
        customer = None;
    
        cursor.execute('SELECT * FROM Customer WHERE email = ?', (_email,));
        customer = cursor.fetchone();
    
        if ( customer == None ):
            return { 'status' : 404 , 'message' : 'Customer not found'};
        else:
            return { 'status' : 200 , 'message' : 'Customer found' , 'data' : customer };

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};
    

# Read - SELECT
def select():
    try:
        customers = [];

        cursor.execute('SELECT * FROM Customer');
        customers = cursor.fetchall();
    
        return { 'status' : 200 , 'message' : 'Select Customers' , 'data': customers };

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};


# UPDATE
def update(_field:str, _cpf:str, _newValue:any):
    try:
        fields = ['name' , 'cpf' , 'email' , 'phone'];

        if ( _field not in fields ):
            return { 'status' : 400, 'message' : 'Invalid field'};

        customerByCpf = findByCPF(_cpf);
    
        if ( customerByCpf['status'] == 404 ):
            return { 'status' : 404 , 'message' : 'Product not found'};

        # Verificar os atributos únicos. Caso seja único, validar o novo valor.
        if ( _field == 'cpf' ):
            customerNewCPF = findByCPF(_newValue);

            if ( customerNewCPF['status'] == 200 ):
                return { 'status' : 400 , 'message' : 'New cpf already registered'};

        if ( _field == 'email'):
            customerNewEmail = findByEmail(_newValue);

            if ( customerNewEmail['status'] == 200 ):
                return { 'status' : 400 , 'message' : 'New email already registered'};

        cursor.execute(f'UPDATE Customer SET {_field} = ? WHERE id = ?', (_newValue , customerByCpf['data'][0]));
        connection.commit();
    
        return { 'status' : 200, 'message' : 'Customer updated'};

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};

# DELETE
def delete(_cpf:str):
    try:
        customerByCPF = findByCPF(_cpf);
    
        if ( customerByCPF['status'] == 404 ):
            return { 'status' : 404 , 'message' : 'Customer not found' };

        cursor.execute('DELETE FROM Customer WHERE id = ?', (customerByCPF['data'][0],));
        connection.commit();
    
        return { 'status' : 410 , 'message' : 'Customer deleted'};
            
    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};