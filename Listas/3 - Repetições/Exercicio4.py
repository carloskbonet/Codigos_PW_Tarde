PpToVote = int(0);
count = int(1);

inputVote = int(0);

# Votos possíveis
candidate1 = int(0);
candidate2 = int(0);
candidate3 = int(0);
candidate4 = int(0);
vNull = int(0);
vBlank = int(0);

print('Eleição em andamento !! Digite quantos candidatos irão votar.');

PpToVote = int(input('Digite: '));

print('Existem 4 candidatos na eleição, sendo representados pelos números : 1 , 2 , 3 e 4.');
print('Digite 5 para votar nulo e 6 para votar em branco.\n\n');

while (count <= PpToVote):
    inputVote = int(input(f'Pessoa {count}, digite seu voto :'));

    if ( inputVote < 1 or inputVote > 6 ):
        print('Voto inválido. Tente novamente. . .');
    else:
        if ( inputVote == 1 ):
            candidate1 = candidate1 + 1;
        if ( inputVote == 2 ):
            candidate2 = candidate2 + 1;
        if ( inputVote == 3 ):
            candidate3 = candidate3 + 1;
        if ( inputVote == 4 ):
            candidate4 = candidate4 + 1;
        if ( inputVote == 5 ):
            vNull = vNull + 1;
        if ( inputVote == 6 ):
            vBlank = vBlank + 1;

        count = count + 1;

print('\nContagem de votos em andamento . . . \n');


print(f'Candidato 1 : {candidate1}');
print(f'Candidato 2 : {candidate2}');
print(f'Candidato 3 : {candidate3}');
print(f'Candidato 4 : {candidate4}');
print(f'Nulo : {vNull}');
print(f'Branco : {vBlank}');