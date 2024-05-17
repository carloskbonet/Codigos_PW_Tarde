import random;

jogos = ['Minecraft' , 'Terraria' , 'Gartic'];
marcasDeCelular = ['Xiaomi' , 'Motorola' , 'Nokia'];
personagensDeLol = ['Gnar' , 'Neymar' , 'Veigar'];

def selectWord():
    contextChoice = random.randint(1 , 3);

    global jogos;
    global marcasDeCelular;
    global personagensDeLol;
    wordChoice = str('');

    if ( contextChoice == 1 ):
        wordChoice = random.choice(jogos);
        print(f'O contexto escolhido é Jogos.')

    if ( contextChoice == 2 ):
        wordChoice = random.choice(marcasDeCelular);
        print(f'O contexto escolhido é Marcas de Celular.')
    
    if ( contextChoice == 3 ):
        wordChoice = random.choice(personagensDeLol);
        print(f'O contexto escolhido é Personagens de um jogo ruim.')

    return wordChoice;


def gameplay(word:str):
    inputTry = str('');

    print(f'\nBoas vindas ao jogo da forca.  Imagine que aqui estão as regras do jogo:');
    print(f'\nQuantidade de letras na palavra escolhida: {len(word)}');
    
    while ( True ):
        print(f'Tente adivinhar a palavra: {'_ ' * len(word)}')

        inputTry = str(input(f'Digite (apenas uma letra): '));

        # Repetição para exibir todas as letras da palavra. Verificar letra por letra.
        # O usuário vai digitar apenas UMA letra, devemos verificar se ela está presente na palavra.
        for i in range( 0 , len(word) ):
            print(word[i]);






selectedWord = str('');

selectedWord = selectWord();

print(f'A palavra escolhida é : {selectedWord}');

gameplay(selectedWord);

