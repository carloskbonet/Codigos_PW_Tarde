import produto;
from os import system;

# Variáveis
inputMenu = int(0);

while ( True ):
    system('cls');
    # Opções do Menu
    print('Operações na tabela produtos.');
    print('Digite 1 para criar um novo produto.');
    print('Digite 2 para buscar pelo nome.');
    print('Digite 3 para listar todos os produtos.');
    
    inputMenu = int(input('Digite: '));

    if ( inputMenu == 1 ):
        print('\nDigite os dados solicitados para criar um novo produto: ');
        name = input('Nome: ');
        price = float(input('Preço: '));
        quantity = int(input('Quantidade: '));
    
        response = produto.create(name , price, quantity);
    
        print(f'\n{response['message']}');


    if ( inputMenu == 3 ):
        print('\nListagem de produtos.');
    
        response = produto.select();
    
        print(response['data']);


    input('\nAperte ENTER para continuar');