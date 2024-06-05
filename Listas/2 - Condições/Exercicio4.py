import datetime;

anoAtual = datetime.datetime.now();

restoDaDivisao = int(0);
nascimento = int(0);
idade = int(0);
ultimaEleicao = int(0);
proximaEleicao = int(0);

print(f'O algoritmo verificará se o usuário poderá votar na próxima eleição\n');

nascimento = int(input('Digite seu ano de nascimento: '));

idade = anoAtual.year - nascimento;

print(f'Sua idade é: {idade} anos\n');

restoDaDivisao = anoAtual.year % 5;

if (  restoDaDivisao == 0  ):
    print(f'\nEstamos em um ano de Eleição.');

    if ( idade >= 16 ):
        print(f'Você pode votar nessa eleição.');
    else:
        print(f'Você NÃO poderá votar na eleição atual.');

else:
    print(f'Não estamos em um ano de Eleição.');

    ultimaEleicao = anoAtual.year - restoDaDivisao;
    proximaEleicao = ultimaEleicao + 5;

    print(f'A última eleição ocorreu em: { ultimaEleicao }');
    print(f'A próxima eleição ocorrerá em : { proximaEleicao }');

    idade = idade - restoDaDivisao + 5;

    print(f'A idade do usuário em {proximaEleicao} será {idade} anos\n');

    if ( idade >= 16 ):
        print(f'Você poderá votar na próxima eleição.');
    else:
        print(f'Você NÃO poderá votar na próxima eleição.');
