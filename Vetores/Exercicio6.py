numbers = [];
inputNumber = int(-1);
result = float(0);
sum = int(0);

# Explicação

print('O algoritmo calculará a soma dos valores pares digitados.');

print('Digite números inteiros. Digite 0 para encerrar.');

while ( inputNumber != 0 ):
    
    inputNumber = int(input('Digite: '));

    if ( inputNumber == 0 ):
        break;
    else:
        numbers.append(inputNumber);


for i in range( 0 , len(numbers) , 1 ):

    result = numbers[i] % 2;

    if ( result == 0 ):
        sum = sum + numbers[i];


print(f'\nResultado da soma: {sum}');