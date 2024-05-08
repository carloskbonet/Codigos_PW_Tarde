
# Variáveis

saldo = float(0);
taxa = float(0);
meses = int(0);
rendimento = float(0);
saldoFinal = float(0);

# Explicação

print('O algoritmo calculará juros simples com base no saldo, taxa e período inseridos.');

# Entrada de Dados

saldo = float(input('Valor na conta: '));
taxa = float(input('Digite a porcentagem de rendimento (0 a 20%): '));
meses = int(input('Vai deixar o valor rendendo por quantos meses? '));

# Processamento

rendimento = (( taxa / 100 ) * saldo) * meses;
saldoFinal = saldo + rendimento;

# Saída de Dados

print(f'Saldo Inicial: {round(saldo , 2)} R$');
print(f'Rendimento Total: {round(rendimento , 2)} R$');
print(f'Saldo Final: {round(saldoFinal , 2)} R$');
