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

print(f'\n{produtos}');

# Variáveis update / delete / find

nomeBusca = str('');
produto = None;

print('\nDigite a informação solicitada para procurar um produto.');
nomeBusca = input('Nome: ');

cursor.execute('SELECT * FROM Produto WHERE nome = ?' , (nomeBusca ,) );
produto = cursor.fetchone();

if ( produto == None ):
    print('\nProduto não encontrado.');
    exit();

print(f'\n{produto}\n');

while ( True ):
    print(f'Digite 1 para atualizar o preço');
    print(f'Digite 2 deletar')
    print(f'Digite 0 para sair');

    userInput = int(input('Digite: '));

    if ( userInput == 1 ):
        print(f'\nVamos atualizar o produto selecionado. Digite os dados solicitados abaixo.');
        novoPreco = float(input('Preço: '));

        cursor.execute('UPDATE Produto SET preco = ? WHERE id = ?', ( novoPreco , produto[0] ) );
        connection.commit();
    
        print('\nProduto atualizado com sucesso.');

    if ( userInput == 2 ):
        
    
        cursor.execute('DELETE FROM Produto WHERE id = ?' , ( produto[0], ));
        connection.commit();

        print('\nProduto deletado com sucesso.');

