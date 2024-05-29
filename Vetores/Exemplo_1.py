

cores = [ 'Azul' , 'Marrom' , 'Verde' , 'Roxo' , 'Vermelho' ];


print(f'Vetor antigo: {cores}');

cores.append('Rosa');
cores.append('Laranja');
cores.append('Azul');
cores.append('Branco e Preto');

print(f'Vetor atualizado: {cores}');


print( f'A cor azul aparece {cores.count('Azul')} vezes no vetor' );

cores.append('Amarelo');
cores.append('Cinza');

print(f'Vetor atualizado: {cores}');

cores.remove('Verde');

print( f'Cor removida: { cores.pop() }' );

print(f'Vetor atualizado: {cores}');