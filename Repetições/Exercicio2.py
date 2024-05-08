numero = int(0);
contador = int(10);
tabuada = int(0);

print('O algoritmo fará a tabuada do número digitado.');

numero = int(input('Digite: '));


# Processamento

while ( contador > 0 ):
    tabuada = numero * contador;

    print(f'{numero} x {contador} = {tabuada}');

    contador = contador - 1;
