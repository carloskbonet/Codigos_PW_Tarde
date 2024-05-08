# Variáveis

valorTotal = float(0);
desconto = float(0);
valorDesconto = float(0);
valorFinal = float(0);

# Explicação
print('Algoritmo para cálculo de desconto bancário');


# Inputs
valorTotal = float(input('Digite o valor do boleto: '));
desconto = float(input('Valor de desconto (0 a 100%) (Não digite %): '));

# Processamento
valorDesconto = valorTotal * (desconto / 100);
valorFinal = valorTotal - valorDesconto;

# Output
print(f'Valor total: {valorTotal}');
print(f'Valor de desconto: {valorDesconto}');
print(f'Valor com desconto: {valorFinal}');