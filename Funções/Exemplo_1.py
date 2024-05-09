

def parOuImpar(num:int) -> int:
    verify = int(0);

    verify = num % 2;

    if (verify == 0):
        return 1;
    else:
        return 0;


number = int(0);
result = int(0);

number = int(input('Digite: '));


result = parOuImpar(number);

if ( result == 1 ):
    print(f'\nO número digitado é PAR.');
else:
    print(f'\nO número digitado é IMPAR.');
