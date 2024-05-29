
numbers = [];
inputNumber = int(1);
hNumber = int(0);

print(f'Preencha o vetor. Digite 0 para parar de inserir.');

while (inputNumber != 0):
    inputNumber = int(input('Digite: '));

    numbers.append(inputNumber);


# Encontra o maior número do vetor.

if ( len(numbers) > 0  ):
    hNumber = numbers[0];

for i in range ( 0 , len(numbers) , 1 ):

    if ( numbers[i] > hNumber ):
        print(f'O maior número era {hNumber} // Novo maior número: {numbers[i]}');
        hNumber = numbers[i];
    
print(f'\nMaior número encontrado: {hNumber}');


