# Variaveis

numero = int(0);
teste_3 = int(0);
teste_5 = int(0);

print('O algoritmo irá verificar se o número digitado é múltiplo de 3 e 5.');

numero = int(input('Digite: '));

teste_3 = numero % 3;
teste_5 = numero % 5;

if ( teste_3 == 0 and teste_5 == 0 ):
    print(f'O número {numero} é múltiplo de 3 e 5.');
else:
    print(f'NÃO é múltiplo de 3 e 5.');