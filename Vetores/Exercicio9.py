numbers = [];
inputNumber = int(0);
sortedBool = bool(True);

print('Digite números. O algoritmo verificará se estão ordenados.');
print('Digite 0 para parar.');

while (True):
    inputNumber = int(input('Digite: '));

    if (inputNumber == 0):
        break;
    else:
        numbers.append(inputNumber);


# Verificar se está ordenado

print(f'\nVetor: {numbers}\n');

for i in range(0 , len(numbers)-1 , 1):
    #print(f'Valor: {numbers[i]}  // Indice: {i}');
    #print(f'Proximo valor: {numbers[i+1]} // Indice: {i+1}');
    #print('-------------------------------------------');

    if ( numbers[i] > numbers[i + 1] ):
        sortedBool = False;


if ( sortedBool == True ):
    print('O vetor está ordenado.');
else:
    print('O vertor NÃO está ordenado.');
    numbers.sort();
    print(f'Vetor ordenado: {numbers}');
