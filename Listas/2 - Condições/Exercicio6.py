peso = float(0);
altura = float(0);
sexo = str('');
imc = float(0);
inputMenu = int(0);

print(f'O algoritmo calculará o IMC do usuário. Preencha o formulário abaixo.');

altura = float(input('Altura: '));
peso = float(input('Peso: '));

print('Para calcular o IMC, precisamos saber o sexo do usuário.');

while (True):
    print(f'\nDigite 1 para feminino');
    print('Digite 2 para masculino');
    inputMenu = int(input('Digite: '));

    if ( inputMenu < 1 or inputMenu > 2 ):
        print(f'Digite apenas números presentes no menu.');

    if ( inputMenu == 1 ):
        sexo = 'F';
        break;
    if ( inputMenu == 2 ):
        sexo = 'M';
        break;


# Processamento

imc = peso / (altura ** 2);

# Output

print(f'O IMC do usuário é: {round(imc , 2)}');

if ( sexo == 'M' ):
    if ( imc < 18.5 ):
        print(f'Abaixo do peso.');
    if ( imc >= 18.5 and imc <= 25 ):
        print(f'Peso normal.');
    if ( imc > 25 and imc <= 30 ):
        print(f'Acima do peso.');
    if ( imc > 30 ):
        print('Obesidade');
if ( sexo == 'F' ):
    if ( imc < 17 ):
        print(f'Abaixo do peso.');
    if ( imc >= 17 and imc <= 23 ):
        print(f'Peso normal.');
    if ( imc > 23 and imc <= 27 ):
        print(f'Acima do peso.');
    if ( imc > 27 ):
        print('Obesidade');