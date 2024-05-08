import os;
import time;

# Variáveis
inputMenu = int(1);
# Variáveis da Tabuada
numero = int(0);
contador = int(10);
tabuada = int(0);

# Explicação
print('Menu de seleção de algoritmos.');
time.sleep(2);

# Processamento

while (inputMenu != 0):
    os.system('cls');

    print('\n------------------------');
    print('Menu de Seleção.');
    print('Digite 1 para acessar o algoritmo da Tabuada.');
    print('Digite 0 para encerrar a aplicação.');

    inputMenu = int(input('Digite: '));

    if (inputMenu == 1):
        # Inserir algoritmo da tabuada.
        contador = 10;
        
        print('O algoritmo fará a tabuada do número digitado.');

        numero = int(input('Digite: '));
    
        while ( contador > 0 ):
            tabuada = numero * contador;

            print(f'{numero} x {contador} = {tabuada}');

            contador = contador - 1;

    if (inputMenu == 0):
        print('\nEncerrando . . .');
        break;

    input('\nAperte ENTER para continuar');
