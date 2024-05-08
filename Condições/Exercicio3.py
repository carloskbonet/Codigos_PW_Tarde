
# Variáveis
nota = float(0);
NOTA_CORTE = float(7);

# Explicação
print(f'O algoritmo verifica se o aluno foi reprovado ou aprovado.')
print(f'A nota será avaliada entre 0 e 10. Sendo a nota de corte 7.');

# Input
nota = float(input('Digite: '));

if ( nota > 10 or nota < 0 ):
    print('Digite apenas notas válidas (0 a 10).');
    exit();

# Saída de Dados

if ( nota >= NOTA_CORTE ):
    print('O aluno está APROVADO.');

if ( nota <= (NOTA_CORTE - 2) ):
    print('O aluno está REPROVADO.');

if ( nota > (NOTA_CORTE - 2) and nota < (NOTA_CORTE - 0.5) ):
    print('O aluno deve fazer o EXAME.');

if ( nota > (NOTA_CORTE - 0.5) and nota < NOTA_CORTE ):
    print('Aluno direcionado ao conselho de classe.');