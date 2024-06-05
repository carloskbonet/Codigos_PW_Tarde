variavel_1 = int(0);
variavel_2 = int(0);
auxiliar = int(0);

print(f'\nO algoritmo irá inverter os valores das variáveis.\n');

variavel_1 = int(input('Digite a variavel A: '));
variavel_2 = int(input('Digite a variavel B: '));

print(f'A: {variavel_1} / B: {variavel_2}');

auxiliar = variavel_1;

variavel_1 = variavel_2;
variavel_2 = auxiliar;


print(f'A: {variavel_1} / B: {variavel_2}');