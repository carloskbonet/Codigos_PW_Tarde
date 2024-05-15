from Conversoes import conversaoIdade;

inputYear = int(0);
inputMonth = int(0);
inputDay = int(0);
result = [];

print(f'Digite sua data de nascimento. Iremos calcular o seu tempo de vida.');

# Entrada de Dados
inputDay = int(input('Dia: '));
inputMonth = int(input('Mês: '));
inputYear = int(input('Ano: '));

#print(f'O usuário tem {resDay} dias, {resMonth} meses e {resYear} anos de vida.');

result = conversaoIdade(inputDay , inputMonth , inputYear);

print(f'Resultado: {result}');