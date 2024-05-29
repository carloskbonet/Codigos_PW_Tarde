
filmes_TV = ['Kung Fu Panda 4', 'Transformers 8', 'Duro de Matar 1', 'Click', 'O Protetor', 'Rambo', 'Jurassic Park'];
movieName = str('');
verify = bool(False);

print(f'Estamos apresentando a lista de filmes disponíveis na TV essa semana.');
print(f'Digite o nome de um filme para verificar se estará disponível.');

movieName = str(input('Digite: '));


for i in range ( 0 , len(filmes_TV) , 1 ):
    if ( movieName == filmes_TV[i] ):
        verify = True;
        break;
    else:
        verify = False;


if ( verify == True ):
    print(f'O filme vai passar na TV essa semana.');
else:
    print(f'Não estará disponível, verifique o catálogo.');