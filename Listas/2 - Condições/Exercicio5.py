nome = str('');
sexo = str('');
estadoCivil = str('');
tempoDeCasamento = int(0);
pronome = str('');
inputMenu = int(0);

print(f'Formulário de Cadastro');

nome = input('Nome: ');

while (True):
    print(f'Digite 1 para Feminino');
    print(f'Digite 2 para Masculino');
    print(f'Digite 3 para não informar');
    inputMenu = int(input('Digite: '));

    if ( inputMenu < 1 or inputMenu > 3 ):
        print('Digite apenas opções presentes no Menu.');

    if ( inputMenu == 1):
        sexo = 'F';
        pronome = 'a';
        break;
    if ( inputMenu == 2 ):
        sexo = 'M';
        pronome = 'o';
        break;
    if ( inputMenu == 3 ):
        sexo = 'ND';
        pronome = 'o';
        break;

print(f'\nPrecisamos saber seu estado civil.');

while (True):
    print(f'Digite 1 para casad{pronome}');
    print(f'Digite 2 para solteir{pronome}');
    inputMenu = int(input('Digite: '));

    if ( inputMenu < 1 or inputMenu > 2 ):
        print('Digite apenas opções presentes no Menu.');

    if ( inputMenu == 1):
        estadoCivil = f'casad{pronome}';
        tempoDeCasamento = int(input(f'Está casad{pronome} a quanto tempo? '));

        break;
    if ( inputMenu == 2 ):
        estadoCivil = f'solteir{pronome}';
        break;


print(f'\nFicha cadastrada:');
print(f'Nome: {nome} / Estado: {estadoCivil}');
if ( estadoCivil == 'casado' or estadoCivil == 'casada' ):
    print(f'{tempoDeCasamento} anos de casamento');