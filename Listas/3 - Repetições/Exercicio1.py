# Declaração de Variáveis
inputStop = int(0);

# Print Explicativo
print('O algoritmo calculará o quadrado dos números iniciando em 1 e encerrando no número digitado.');


# Input
inputStop = int(input('Digite: '));


# Processamento / Output

for i in range( 1 , inputStop+1 , 1 ):

    print(i ** 2);
