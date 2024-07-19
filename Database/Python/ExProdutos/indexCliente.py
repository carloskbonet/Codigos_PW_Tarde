import cliente;
from os import system;

# Variáveis
inputMenu = int(0);

while ( True ):
    system('cls');
    # Opções do Menu
    print('Operações na tabela cliente.');
    print('Digite 1 para criar.');
    print('Digite 2 para buscar pelo cpf.');
    print('Digite 3 para buscar pelo email.');
    print('Digite 4 para listar.');
    print('Digite 5 para deletar.');
    print('Digite 6 para atualizar.');

    inputMenu = int(input('Digite: '));

    if ( inputMenu == 1 ):
        print('\nDigite os dados solicitados para criar um novo cliente: ');
        try:
            name = input('Nome: ');
            cpf = input('CPF: ');
            email = input('Email: ');
            phone = input('Telefone: ');
        
            response = cliente.create(name , cpf , email , phone);
        
            print(f'\n{response['message']}');
        except:
            print('Something went wrong');

    if ( inputMenu == 2 ):
        print('\nVamos procurar um cliente específico.');
        try:
            cpf = input('CPF: ');

            response = cliente.findByCPF(cpf);
        
            print(f'\n{response['message']}');
        
            if ( response['status'] == 200 ):
                print(f'\nID / NOME / CPF / EMAIL / PHONE');
                print(f'{response['data'][0]} / {response['data'][1]} / {response['data'][2]} / {response['data'][3]} / {response['data'][4]} ');

        except:
            print('Something went wrong');

    if ( inputMenu == 3 ):
        print('\nVamos procurar um cliente específico.');
        try:
            email = input('Email: ');

            response = cliente.findByEmail(email);
        
            print(f'\n{response['message']}');
        
            if ( response['status'] == 200 ):
                print(f'\nID / NOME / CPF / EMAIL / PHONE');
                print(f'{response['data'][0]} / {response['data'][1]} / {response['data'][2]} / {response['data'][3]} / {response['data'][4]} ');

        except:
            print('Something went wrong');

    if ( inputMenu == 4 ):
        print('\nListagem de clientes.');
    
        response = cliente.select();
    
        if ( response['status'] == 200 ):
            
            print(f'\nID / NOME / CPF / EMAIL / PHONE');
            for customer in response['data']:     
                print(f'{customer[0]} / {customer[1]} / {customer[2]} / {customer[3]} / {customer[4]} ');

        else:
            print(response['message']);
    
    if ( inputMenu == 5 ):
        print('\nDeletar um cliente.');
        try:
            cpf = input('cpf: ');
        
            response = cliente.delete(cpf);
        
            print(f'\n{response['message']}');

        except:
            print('Something went wrong');


    if ( inputMenu == 6 ):
        print('\nMenu de atualização do produto.');
        print('Digite 1 para atualizar o nome');
        print('Digite 2 para atualizar o cpf');
        print('Digite 3 para atualizar a email');
        print('Digite 4 para atualizar a telefone');

        try:
            subInputMenu = int(input('Digite: '));


            cpf = input('CPF: ');

            customerByCPF = cliente.findByCPF(cpf);

            if ( customerByCPF['status'] == 200 ):
                print(f'\nID / NOME / CPF / EMAIL / PHONE');
                print(f'{response['data'][0]} / {response['data'][1]} / {response['data'][2]} / {response['data'][3]} / {response['data'][4]} ');

                if ( subInputMenu == 1 ):
                    print('\nAtualizando o nome.');
                    newName = input('Novo Nome: ');

                    response = cliente.update('name' , cpf , newName);
                
                    print(f'\n{response['message']}');


                if ( subInputMenu == 2 ):
                    print('\nAtualizando o CPF.');
                    newCpf = input('CPF: ');
            
                    response = cliente.updatePrice('cpf' , cpf , newCpf);
            
                    print(f'\n{response['message']}');
            
                if ( subInputMenu == 3 ):
                    print('\nAtualizando o email.');
                    newEmail = int(input('Email: '));
            
                    response = cliente.update('email' , cpf , newEmail);
            
                    print(f'\n{response['message']}');
            
                if ( subInputMenu == 4 ):
                    print('\nAtualizando o telefone.');
                    newPhone = int(input('Telefone: '));
            
                    response = cliente.update('phone' , cpf , newPhone);
            
                    print(f'\n{response['message']}');


            else:
                print(f'\n{customerByCPF['message']}');

        except:
            print('Something went wrong');

    input('\nAperte ENTER para continuar');