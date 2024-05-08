
contador = int(0);

print('O algoritmo fará uma contagem regressiva a partir do número digitado.\n');



while (contador < 1):
    contador = int(input('Digite: '));

    if (contador < 1):
        print('Digite apenas números positivos.\n');

# Processamento

while (contador >= 0):
    print(contador);

    contador = contador - 1;