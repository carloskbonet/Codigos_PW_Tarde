count = int(2);
inputNumber = int(0);
fatorial = int(1);

print('O algoritmo calculará o fatorial do número digitado.');

inputNumber = int(input('Digite: '));

while ( count <= inputNumber ):

    print(f'{fatorial} x {count}');

    fatorial = fatorial * count;

    count = count + 1;


print(f'Resultado: {fatorial}');