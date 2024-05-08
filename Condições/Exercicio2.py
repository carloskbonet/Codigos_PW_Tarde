# ALGORITMO PARA VERIFICAR PAR OU IMPAR

# Variáveis
numero = float(0);
resultado = float(0);

# Explicação
print('O algoritmo verficará se o número digitado é PAR ou IMPAR.\n');

# Inputs
numero = float(input('Digite: '));

# Processamento
resultado = numero % 2;

# Saída de Dados

if ( resultado == 0 ):
    print(f'{numero} é PAR');
if ( resultado != 0 ):
    print(f'{numero} é IMPAR');