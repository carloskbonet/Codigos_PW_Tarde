
cores = [ 'Azul' , 'Marrom' , 'Verde' , 'Roxo' , 'Vermelho' ];
inputNumber = int(0);

#inputNumber = int(input('Digite: '));

#if ( inputNumber >= len(cores) ) :
#    print(f'O vetor NÃO possui a posição {inputNumber}');
#else:
#    print(f'Posição Válida');


alturas = [ 1.8 , 1.65 , 1.89 , 1.79 , 1.81 , 1.76 ];
soma = float(0);
count = int(0);

#for i in range(0 , len(alturas) , 1):
#    print(alturas[i]);
#    soma = soma + alturas[i];

while ( count < len(alturas) ):
    print( alturas[count] );
    soma = soma + alturas[count];

    count = count + 1;

print(f'Soma das alturas {soma} ');
print(f'Média: { soma / len(alturas) }');