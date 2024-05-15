from Juros import jurosCompostos;

initial_value = float(0);
tax = float(0);
months = int(0);
total_value = float(0);

# Print Explicativo
print('O algoritmo solicitará valores para calcular juros compostos.');

# Entrada de Dados
initial_value = float(input('Valor Inicial: '));
tax = float(input('Taxa (0 a 100): '));
months = int(input('Meses: '));

# Processamento

total_value = jurosCompostos(initial_value , tax , months);


print(f'\nValor final: {round(total_value , 2)}');