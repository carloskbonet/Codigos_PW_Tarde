fahrenheit = float(0);
celsius = float(0);

print(f'\nO algoritmo calculará a temperatura em F° para C°\n');

# Input
fahrenheit = float(input('Digite: '));


# Processamento
celsius = (fahrenheit - 32) / 1.8;

# Output
print(f'Resultado: {celsius}');
