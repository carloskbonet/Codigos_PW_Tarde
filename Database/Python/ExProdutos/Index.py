import cliente;
import produto;
import pedido;
from indexCliente import customerMenu;
from indexProduto import productMenu;
from os import system;

# Variáveis
inputMenu = int(0);

while ( True ):
    system('cls');
    # Opções do Menu
    print('Operações na tabela pedidos.');
    print('Digite 1 para criar.');
    print('Digite 2 para buscar pelo código.');
    print('Digite 3 para listar.');
    print('Digite 4 para deletar.');
    print('Digite 5 para atualizar.');
    print('Digite 6 para acessar o CRUD do cliente.');
    print('Digite 7 para acessar o CRUD do produto.');



    inputMenu = int(input('Digite: '));

    if ( inputMenu == 1 ):
        print('\nDigite os dados solicitados para criar um novo pedido: ');
        try:
            code = input('Código: ');
            value = float(input('Valor: '));
            quantity = int(input('Quantidade: '));
            customerCpf = input('CPF: ');
            productName = input('Produto: ');

            response = pedido.create(code , value , quantity , customerCpf , productName);
        
            print(f'\n{response['message']}');
        except:
            print('Something went wrong');

    if ( inputMenu == 2 ):
        print('\nVamos procurar um pedido específico.');
        try:
            code = input('Código: ');

            response = pedido.findByCode(code);
        
            print(f'\n{response['message']}');
        
            if ( response['status'] == 200 ):
                print(f'\nID / CÓDIGO / VALOR / QUANTIDADE'); 
                print(f'{response['request'][0]} / {response['request'][1]} / {response['request'][2]} / {response['request'][3]}');
                print(f'{response['customer'][0]} / {response['customer'][1]} / {response['customer'][2]} / {response['customer'][3]} / {response['customer'][4]}');
                print(f'{response['product'][0]} / {response['product'][1]} / {response['product'][2]} / {response['product'][3]}');

        except:
            print('Something went wrong');

    if ( inputMenu == 3 ):
        print('\nListagem de pedidos.');
    
        response = pedido.select();
    
        if ( response['status'] == 200 ):
            
            print(f'\nID / CÓDIGO / VALOR / QUANTIDADE');
            for request in response['data']:     
                print(f'{request[0]} / {request[1]} / {request[2]} / {request[3]} / {request[4]} / {request[5]}');

        else:
            print(response['message']);
    
    if ( inputMenu == 4 ):
        print('\nDeletar um pedido.');
        try:
            code = input('Código: ');
        
            response = pedido.delete(code);
        
            print(f'\n{response['message']}');

        except:
            print('Something went wrong');
    
    if ( inputMenu == 6 ):
        customerMenu();
    
    if ( inputMenu == 7 ):
        productMenu();

    input('\nAperte ENTER para continuar');
