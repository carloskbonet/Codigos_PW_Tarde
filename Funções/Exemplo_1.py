
def parOuImpar(num:int):
    verify = int(0);

    verify = num % 2;

    if (verify == 0):
        return "PAR";
    else:
        return "IMPAR";


number = int(0);
result = str('');

number = int(input('Digite: '));


result = parOuImpar(number);

print(f'O resultado é: {result}');
