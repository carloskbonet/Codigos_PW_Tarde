from os import system;
from time import sleep;
from random import randint;


# Game data
level = 1;
pontuation = int(0);
timeBetweenLevels = float(1);

# Random
sequence = str('');
randomNumber = int(0);

# User Inputs
userInput = str('');
tryAgain = str('');



# Explicação
print('Bem vindos ao jogo da memória !!         - Não indicado para maiores de 60 anos');
print('Teste sua memória armazenando o maior nível alcançado.');
print('Dica: A resposta deve ser uma sequência em apenas UMA linha.');

input('\nAperte ENTER para continuar');

print('\nIniciando . . .');
sleep(1);

while ( True ):
    system('cls');
    print(f'\nNível: {level}');
    print(f'Pontuação: {pontuation}');
    sleep(1.5);
    # Limpando a string de sequência
    sequence = '';

    # Geração de números aleatórios
    for i in range( 0 , level , 1 ):
        randomNumber = randint(0 , 9);

        sequence = sequence + str(randomNumber);


    # Exibir os números na tela
    for i in range(0 , len(sequence) , 1):
        system('cls');
        print( sequence[i] );
        sleep(timeBetweenLevels);

    # Input do usuário
    system('cls');
    userInput = input('\nAdivinhe a sequência: ');

    # Correção da resposta do usuário.
    userInput = userInput.strip(',.;');


    # Verificação de Acerto / Erro.
    if ( userInput == sequence ):
        print(f'Boaaaaa, agora bora pro próximo.');
        pontuation = pontuation + ( level ** 2 );

        if ( timeBetweenLevels > 0.5 ):
            timeBetweenLevels = timeBetweenLevels - 0.05;
        level = level + 1;

    else:
        print(f'F');
        
        while ( True ):
            tryAgain = input('Digite Y para jogar novamente e N para desistir: ');

            if (tryAgain.lower() != 'y' and tryAgain.lower() != 'n'):
                print('Digita certo mané');
            else:
                break;

        if ( tryAgain.lower() == 'y' ):
            level = 1;
        else:
            print('\nF mesmo :(');
            exit();

    
    input('\nAperte ENTER para continuar');
    
