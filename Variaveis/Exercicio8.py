
idade = int(0);
dias = int(0);
meses = int(0);

print('O algoritmo converterá a idade digitada em dias e meses.');

idade = int(input('Digite uma idade (em Anos): '));

# Processamento

dias = idade * 365;

meses = idade * 12;

print(f'Você tem {idade} anos');
print(f'Conversão para Dias: {dias}');
print(f'Conversão para Meses: {meses}');

