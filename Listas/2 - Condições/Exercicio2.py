a = int(0);
b = int(0);
c = int(0);

print(f'Os valores digitados serão exibidos em ordem decrescente\n');

a = int(input('Digite: '));
b = int(input('Digite: '));
c = int(input('Digite: '));


# Processamento / Output

# Variavel 1 é a maior
if ( a > b and a > c ):
    print(f'{a}');

    if ( b >= c ):
        print(b);
        print(c);
    else:
        print(c);
        print(b);


# Variavel 2 é a maior
if ( b > a and b > c ):
    print(f'{b}');

    if ( a >= c ):
        print(a);
        print(c);
    else:
        print(c);
        print(a);


# Variavel 3 é a maior
if ( c > a and c > b ):
    print(f'{c}');

    if ( a >= b ):
        print(a);
        print(b);
    else:
        print(b);
        print(a);

if ( a == b and a == c ):
    print(a);
    print(b);
    print(c);