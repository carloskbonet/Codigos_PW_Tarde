nivel = int(0);

print('O algoritmo exibirá uma pirâmide de asteriscos. Digite a quantidade de linhas presentes na pirâmide.');

nivel = int(input('Digite: '));

for i in range( 1 , nivel+1 , 1):

    print(  ' ' * (nivel - i)    +    '*' * (2 * i - 1));