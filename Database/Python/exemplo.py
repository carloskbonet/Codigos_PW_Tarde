import sqlite3;


# Variável de conexão com o banco de dados
connection = sqlite3.connect('database.db');

# Tradutor de comandos SQL
cursor = connection.cursor();

# Variáveis do INSERT
nome = str('');
preco = float(0);
quantidade = int(0);
userInput = int(0);
produtos = [];

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produto (
        id  INTEGER PRIMARY KEY,
        nome VARCHAR(64) NOT NULL,
        preco FLOAT NOT NULL,
        quantidade INTEGER NOT NULL
    );
''');

print( f'Dados para a inserção do produto:');

while ( True ):
    print('\nDeseja criar um novo produto? 1 = Sim / 2 = Não.');
    userInput = int(input('Digite: '));

    if ( userInput == 1 ):
        # Inputs
        nome = input('Nome:');
        preco = float(input('Preço: '));
        quantidade = int(input('Quantidade: '));

        cursor.execute(' INSERT INTO Produto (nome,preco,quantidade) VALUES (? , ? , ?) ' , ( nome , preco , quantidade ) );
        connection.commit();

        break;
    if ( userInput == 2 ):
        break;


cursor.execute('SELECT * FROM Produto');
produtos = cursor.fetchall();

print(f'\{produtos}');