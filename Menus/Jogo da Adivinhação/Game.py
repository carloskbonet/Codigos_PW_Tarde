# Importações
import random;
import time;
import os;

# Variáveis
sortedNumber = int(0);
inputDif = int(0);
inputMenu = int(0);
inputTry = int(0);
inputTips = bool(False);

#Variáveis de gameplay
tries = int(4);
tips = int(3);
maxTips = int(3);

# Explicação do Jogo (O menu deve conter TODAS as informações do jogo)
print('Regras do jogo da adivinhação:');
print('Você tem 4 tentativas e 3 dicas por padrão. \nTente adivinhar o número e teste sua sorte.\n');

while (True):
    print('\nDigite 1 para iniciar uma partida\nDigite 0 para encerrar o jogo');

    inputMenu = int(input('Digite: '));
    
    if ( inputMenu < 0 or inputMenu > 1 ):
        print('Não temos essa opção no menu, devo marcar um exame de vista? 😂');

    if ( inputMenu == 0 ):
        print('\nSaindo . . .\n');
        exit(0);

    if ( inputMenu == 1 ):
        # Seleção de Dificuldade (Gerar o número de acordo com a dificuldade)
        print('Menu de seleção de dificuldade.');
        print('Digite 1 para o Fácil (1 a 30)');
        print('Digite 2 para o Normal (1 a 50)');
        print('Digite 3 para o Dificil (1 a 90)')

        while ( True ):
            inputDif = int(input('Digite: '));

            if (inputDif < 1 or inputDif > 3):
                print('Essa dificuldade não existe 🥴.');
            else:
                break;

        if ( inputDif == 1 ):
            sortedNumber = random.randint(1 , 30);
            maxTips = 4;
            print('Só quer mamão? Tudo doce, tudo fácil?\n');

        if ( inputDif == 2 ):
            sortedNumber = random.randint(1 , 50);
            maxTips = 3;
            print('😒 nada demais\n');

        if ( inputDif == 3 ):
            sortedNumber = random.randint(1 , 90);
            maxTips = 2;
            print('☠️ Esse jogo não foi planejado pra isso, cuidado\n');

        tries = 4;
        tips = maxTips;

        print('Iniciando partida . . .');
        time.sleep(1);
        print('3 . . .');
        time.sleep(1);
        print('2 . .');
        time.sleep(1);
        print('1 . Boa sorte.');
        time.sleep(1);

        os.system('cls');

        while ( True ):
            print(f'TESTE: o número é : {sortedNumber}');
            inputTry = int(input('\nTente adivinhar o número.\nDigite: '));

            tries = tries - 1;

            if ( inputTry == sortedNumber ):
                print(f'Uaaaaaaaaaaaaaaaaaaaa você acertou mesmo!! Parabéns, nunca duvidei do seu potencial 🤯');
                print(f'Sobraram {tries} tentativas e {tips} dicas.');
            
                time.sleep(3);
                break;

            else:
                print(f'Errooooou !! 😐🤨☹️😓☠️');
                if ( tries == 1 ):
                    print(f'Estou sentindo . . . na próxima você consegue, boa sorte!!');
            
                if ( tips > 0 ):
                    inputTips = bool(input('Deseja uma dica? (Apenas pressione ENTER para recusar): '));

                    if (inputTips == True):
                        tips = tips -1;

                        if( inputTry < sortedNumber ):
                            if ( (inputTry - sortedNumber) > -10  ):
                                print('Um pouco acima, quase lá 😐.');
                            else:
                                print('Definitivamente um número.');
                        
                        if( inputTry > sortedNumber ):
                            if ( (inputTry - sortedNumber) < 10  ):
                                print('Um pouco abaixo, quase lá 😓.');
                            else:
                                print('Definitivamente um número.');

            if ( tries <= 0 ):
                print(f'\nSinto muito jogador . . .\nGame Over.\n');
                
                input('Aperte ENTER para continuar.');
                os.system('cls');
                break;

    

