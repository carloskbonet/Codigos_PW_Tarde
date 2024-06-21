

// Alternativas de temas:
// Programas de TV / Novelas / Filmes / etc...
// Séries de sites pagos com streaming de video
// Músicas / Estilos musicais
// Esportes
// Jogos / Animes

questions = [
    {
        // MJ
        question : 'Qual é o estilo musical ?',
        a : 'Jazz',
        b : 'Pop',
        c : 'MPB',
        d : 'Samba',
        answer : 'b'
    },
    {
        // K F P
        question : 'Quem é o cantor?',
        a : 'Stevie Wonder',
        b : 'James Hetfield',
        c : 'Eddie Vedder',
        d : "Jack Black",
        answer : 'd'
    },
    {   
        // Ka
        question : 'Qual é o estilo musical ?',
        a : 'Jazz',
        b : 'Pop',
        c : 'MPB',
        d : 'Samba',
        answer : 'c'
    },
    {
        // I U 2
        question : 'Essa música vem de qual filme?',
        a : 'Velozes e Furiosos 3 Desafio em Tóquio',
        b : 'Irmão Urso 2',
        c : 'A era do Gelo 3',
        d : 'Rio 2',
        answer : 'b'
    },
    {
        // M C Ma
        question : 'Quem é o cantor?',
        a : 'Tim Maia',
        b : 'MC Marcinho',
        c : 'Padre Fabio de Melo',
        d : 'Gal Costa',
        answer : 'a'
    },
    {
        //
        question : 'Essa fala é o bordão de qual personagem?',
        a : 'Jack Sparrow',
        b : 'Jake o Cão',
        c : 'Peter Griffin',
        d : 'Homer Simpson',
        answer : 'd'
    }
];



var round = 1;
const roundHTML = document.getElementById('round');
const question = document.getElementById('question'); 
const altA = document.getElementById('altA');
const altB = document.getElementById('altB');
const altC = document.getElementById('altC');
const altD = document.getElementById('altD');


function updateInfos() {
    roundHTML.textContent = round;
    question.textContent = questions[round-1].question;
    altA.textContent = questions[round-1].a;
    altB.textContent = questions[round-1].b;
    altC.textContent = questions[round-1].c;
    altD.textContent = questions[round-1].d;
}

updateInfos();

// A variável "alt" pode ter os valores : 'a' , 'b' , 'c' ou 'd'
function answer(alt) {
    // Verificar se "alt" é igual à resposta da questão.
    // Se a resposta for SIM, então podemos incrementar a variável "rounds" e atualizar a interface novamente.
    // Se a resposta for NÃO, podemos encerrar o jogo ou decrementar o número de tentativas. (Tentativas são opcionais)

    if ( alt == questions[round-1].answer ) {
        console.log('Acertou');

        if ( round < questions.length ) {
            round = round + 1;
            updateInfos();
        }
        else{
            alert('Acabaram as questões');
            window.location.replace('./index.html');
        }
    }
    else {
        console.log('Errou');
    }


}