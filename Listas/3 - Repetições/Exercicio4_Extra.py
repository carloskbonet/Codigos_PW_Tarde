PpToVote = [ 'Maria' , 'Pedro' , 'Ana Clara' , 'Beatriz' , 'Mauro' ];
count = int(0);

inputVote = int(0);

# Votos possíveis
voteOptions = [None, 0 , 0 , 0 , 0 , 0 , 0];

print('Eleição em andamento.');

print('Existem 4 candidatos na eleição, sendo representados pelos números : 1 , 2 , 3 e 4.');
print('Digite 5 para votar nulo e 6 para votar em branco.\n\n');

while (count < len(PpToVote)):
    inputVote = int(input(f'{PpToVote[count]}, digite seu voto :'));

    if ( inputVote < 1 or inputVote > 6 ):
        print('Voto inválido. Tente novamente. . .');
    else:
        voteOptions[inputVote] += 1; 

        count = count + 1;

print('\nContagem de votos em andamento . . . \n');


print(f'Candidato 1 : {voteOptions[1]}');
print(f'Candidato 2 : {voteOptions[2]}');
print(f'Candidato 3 : {voteOptions[3]}');
print(f'Candidato 4 : {voteOptions[4]}');
print(f'Nulo : {voteOptions[5]}');
print(f'Branco : {voteOptions[6]}');