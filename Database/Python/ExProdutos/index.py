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
    print('Digite 4 para deletar um produto.');

    inputMenu = int(input('Digite: '));

    if ( inputMenu == 1 ):
        print('\nDigite os dados solicitados para criar um novo produto: ');
        try:
            name = input('Nome: ');
            price = float(input('Preço: '));
            quantity = int(input('Quantidade: '));
        
            response = produto.create(name , price, quantity);
        
            print(f'\n{response['message']}');
        except:
            print('Something went wrong');

    if ( inputMenu == 2 ):
        print('\nVamos procurar um produto específico.');
        try:
            name = input('Nome: ');

            response = produto.findByName(name);
        
            print(f'\n{response['message']}');
        
            if ( response['status'] == 200 ):
                print(f'\nID / NOME / PREÇO / QUANTIDADE');
                print(response['data']);

        except:
            print('Something went wrong');

    if ( inputMenu == 3 ):
        print('\nListagem de produtos.');
    
        response = produto.select();
    
        if ( response['status'] == 200 ):
            
            print(f'\nID / NOME / PREÇO / QUANTIDADE');
            for product in response['data']: 
                print(product);

        else:
            print(response['message']);
    
    if ( inputMenu == 4 ):
        print('\nDeletar um produto.');
        try:
            name = input('Nome: ');
        
            response = produto.delete(name);
        
            print(f'\n{response['message']}');

        except:
            print('Something went wrong');


    input('\nAperte ENTER para continuar');