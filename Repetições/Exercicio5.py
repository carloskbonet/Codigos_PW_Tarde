# Variáveis para definir a repetição
count = int(3);
inputNumber = int(0);
# Variáveis para calcular Fibonacci
anterior = int(0);
atual = int(1);
proximo = int(0);

print(f'O algoritmo exibirá números da sequência fibonacci.');

inputNumber = int(input('Deseja gerar quantos números ? '));

print(f'1º Número: {anterior}');
print(f'2º Número: {atual}');

while ( count <= inputNumber ):

    proximo = anterior + atual;

    print(f'{count}º Número: {proximo}');

    anterior = atual;
    atual = proximo;

    count = count + 1;