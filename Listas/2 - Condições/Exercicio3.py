PASSWORD = 'a-very-veeeery-long-password';
inputPassword = str('');

print(f'Login.\n');

inputPassword = input('Senha: ');

if ( inputPassword == PASSWORD ):
    print(f'\nLogged In');
else:
    print(f'\nNot Authorized');