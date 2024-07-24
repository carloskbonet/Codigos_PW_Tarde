# Back-end

import sqlite3;
from cliente import findByCPF;
from produto import findByName;
import cliente;
import produto;

connection = sqlite3.connect('store.db');
cursor = connection.cursor();

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Request (
        id INTEGER PRIMARY KEY,
        code VARCHAR(16) UNIQUE NOT NULL,
        value FLOAT NOT NULL,
        quantity INTEGER NOT NULL,
        
        customerId INTEGER NOT NULL,
        productId INTEGER NOT NULL,
        
        FOREIGN KEY (customerId) REFERENCES Customer(id),
        FOREIGN KEY (productId) REFERENCES Product(id)
    );
'''
);


# CREATE
def create(_code:str , _value:float , _quantity:int, _customerCPF:str , _productName:str):
    try:
        # Verificar todos os campos "unique". Impossibilitar a criação caso existam valores duplicados.
        requestByCode = findByCode(_code);

        if ( requestByCode['status'] == 200 ):
            return { 'status' : 403 , 'message' : 'Code already registered'};
    
        # Encontrar os IDs das chaves estrangeiras.
        customerByCPF = findByCPF(_customerCPF);

        if ( customerByCPF['status'] == 404 ):
            return { 'status' : 404, 'message' : 'Customer not found' };
    
        productByName = findByName(_productName);

        if ( productByName['status'] == 404 ):
            return { 'status' : 404, 'message' : 'Product not found' };

        # Criação
        cursor.execute('INSERT INTO Request (code,value,quantity, customerId, productId) VALUES (?,?,?,?,?)' , (_code, _value , _quantity , customerByCPF['data'][0] , productByName['data'][0] ));
        connection.commit();
    
        return { 'status' : 201 , 'message' : 'Request created'};

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};




# READ - FIND
def findByCode(_code:str):
    try:
        request = None;

        cursor.execute('SELECT * FROM Request WHERE code = ?' , (_code,));
        request = cursor.fetchone();
    
        if ( request == None ):
            return { 'status' : 404 , 'message' : 'Request not found'};
        else:
            customerById =  cliente.findById( request[4] );
            productById = produto.findById( request[5] );


            #return { 'status' : 200 , 'message' : 'Request found' , 'data' : { 'request' : request , 'customer' : customerById , 'product' : productById } };

            return { 'status' : 200 , 'message' : 'Request found' , 'request' : request , 'customer' : customerById['data'] , 'product' : productById['data'] };

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};

# READ - SELECT
def select():
    try:
        requests = [];

        cursor.execute('SELECT * FROM Request');
        requests = cursor.fetchall();
    
        return { 'status' : 200 , 'message' : 'Select Requests' , 'data': requests };

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};

# UPDATE
def update(_field:str , _code:str , _newValue:any):
    try:
        fields = ['code' , 'value' , 'quantity', 'customerId' , 'productId'];

        if ( _field not in fields ):
            return { 'status' : 400, 'message' : 'Invalid field'};

        requestByCode = findByCode(_code);
    
        if ( requestByCode['status'] == 404 ):
            return { 'status' : 404 , 'message' : 'Request not found'};

        # Verificar os atributos únicos. Caso seja único, validar o novo valor.
        if ( _field == 'code' ):
            requestNewCode = findByCode(_newValue);

            if ( requestNewCode['status'] == 200 ):
                return { 'status' : 400 , 'message' : 'New code already registered'};
    
        # Verificar os atributos de chave estrangeira
        if ( _field == 'customerId' ):
            customerByCPF = findByCPF(_newValue);

            if ( customerByCPF['status'] == 404 ):
                return { 'status' : 404, 'message' : 'Customer not found' };
            else:
                _newValue = customerByCPF['data'][0];
        
        if ( _field == 'productId' ):
            productByName = findByName(_newValue);
            
            if ( productByName['status'] == 404 ):
                return { 'status' : 404, 'message' : 'Product not found' };
            else:
                _newValue = productByName['data'][0];  
                

        cursor.execute(f'UPDATE Request SET {_field} = ? WHERE id = ?', (_newValue , requestByCode['data'][0]));
        connection.commit();
    
        return { 'status' : 200, 'message' : 'Request updated'};

    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};
# DELETE
def delete(_code:str):
    try:
        requestByCode = findByCode(_code);
    
        if ( requestByCode['status'] == 404 ):
            return { 'status' : 404 , 'message' : 'Request not found' };

        cursor.execute('DELETE FROM Request WHERE id = ?', (requestByCode['data'][0],));
        connection.commit();
    
        return { 'status' : 410 , 'message' : 'Request deleted'};
            
    except:
        return { 'status' : 500 , 'message' : 'Internal Error'};