numero_1 = int(0);
numero_2 = int(0);
numero_3 = int(0);
soma = int(0);


print(f'Testes de Condições');

numero_1 = int(input('Digite: '));
numero_2 = int(input('Digite: '));
numero_3 = int(input('Digite: '));

# Processamento / Output

soma = numero_1 + numero_2;

print(f'\nSoma:{soma} / C:{numero_3}\n');

if ( soma > numero_3 ):
    print(f'A soma é MAIOR que C');
else:
    if ( soma < numero_3 ):
        print(f'A soma é MENOR que C');
    else:
        print(f'A soma é IGUAL a C');
