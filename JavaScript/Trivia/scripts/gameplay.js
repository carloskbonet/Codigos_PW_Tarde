

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
        answer : 'b',
        mp3: '../mp3/Quest1.mp3'
    },
    {
        // K F P
        question : 'Quem é o cantor?',
        a : 'Stevie Wonder',
        b : 'James Hetfield',
        c : 'Eddie Vedder',
        d : "Jack Black",
        answer : 'd',
        mp3: '../mp3/Quest1.mp3'
    },
    {   
        // Ka
        question : 'Qual é o estilo musical ?',
        a : 'Jazz',
        b : 'Pop',
        c : 'MPB',
        d : 'Samba',
        answer : 'c',
        mp3: '../mp3/Quest1.mp3'
    },
    {
        // I U 2
        question : 'Essa música vem de qual filme?',
        a : 'Velozes e Furiosos 3 Desafio em Tóquio',
        b : 'Irmão Urso 2',
        c : 'A era do Gelo 3',
        d : 'Rio 2',
        answer : 'b',
        mp3: '../mp3/Quest1.mp3'
    },
    {
        // M C Ma
        question : 'Quem é o cantor?',
        a : 'Tim Maia',
        b : 'MC Marcinho',
        c : 'Padre Fabio de Melo',
        d : 'Gal Costa',
        answer : 'a',
        mp3: '../mp3/Quest1.mp3'
    },
    {
        //
        question : 'Essa fala é o bordão de qual personagem?',
        a : 'Jack Sparrow',
        b : 'Jake o Cão',
        c : 'Peter Griffin',
        d : 'Homer Simpson',
        answer : 'd',
        mp3: '../mp3/Quest1.mp3'
    }
];

// Receber parâmetros da interface anterior.
const parameter = new URLSearchParams(window.location.search);
const timeFromParameter = parameter.get('time');


var round = 1;
const roundHTML = document.getElementById('round');
const question = document.getElementById('question'); 
const altA = document.getElementById('altA');
const altB = document.getElementById('altB');
const altC = document.getElementById('altC');
const altD = document.getElementById('altD');

// MP3 play
const playMp3Btn = document.getElementById('playbtn');
var audio = undefined;

// Tentativas e pontuação
const triesFromHTML = document.getElementById('tries');
const pontuationFromHTML = document.getElementById('pontuation');

// Temporizador
const timerFromHTML = document.getElementById('timer');

var timerID = undefined;
var pontuation = 0;
var tries = 3;
var timeToAnswer = ( timeFromParameter * 1000 );


function updateInfos() {
    roundHTML.textContent = round;
    question.textContent = questions[round-1].question;
    altA.textContent = questions[round-1].a;
    altB.textContent = questions[round-1].b;
    altC.textContent = questions[round-1].c;
    altD.textContent = questions[round-1].d;
    triesFromHTML.textContent = `Tentativas : ${tries}`;
    pontuationFromHTML.textContent = `${pontuation} Pontos.`;

    updateTimer();
}

updateInfos();

// A variável "alt" pode ter os valores : 'a' , 'b' , 'c' ou 'd'
function answer(alt) {
    // Verificar se "alt" é igual à resposta da questão.
    // Se a resposta for SIM, então podemos incrementar a variável "rounds" e atualizar a interface novamente.
    // Se a resposta for NÃO, podemos encerrar o jogo ou decrementar o número de tentativas. (Tentativas são opcionais)

    clearTimeout(timerID);
    timeToAnswer = ( timeFromParameter * 1000 );
    if ( audio != undefined )
        audio.pause();

    if ( alt == questions[round-1].answer ) {
        console.log('Acertou');

        if ( round < questions.length ) {
            round = round + 1;
            
            // Adicionar pontuação nesta sessão
            pontuation = pontuation + ( round ** 2 );

            alert('Acertou 😎👌👌👌');
            updateInfos();
        }
        else{
            alert(`Acabaram as questões.\nPontuação final: ${pontuation}`);
            window.location.replace('./index.html');
        }
    }
    else {
        //Adicionar punição nesta sessão
        if ( tries > 0 ) {
            tries = tries -1;

            pontuation = pontuation / 2;
        }

        if ( tries <= 0 ) {
            // Acabaram as tentativas
            alert('Game Over');
            window.location.replace('./index.html');
        }
        else{
            // Passar para a próxima questão
            if ( round < questions.length ) {
                round = round + 1;

                alert('Errou ☠️😐😓');
                updateInfos();
            }
        }
    }

}

function updateTimer() {

    if ( timeToAnswer > 0 ) {
        timerFromHTML.textContent = timeToAnswer / 1000;

        timeToAnswer = timeToAnswer - 1000;
        timerID = setTimeout( updateTimer , 1000 );
    }
    else {
        timeOut();
    }
}


function timeOut() {
    alert('O tempo acabou.');
    window.location.replace('./index.html');
}



function playMp3() {
    audio = new Audio(questions[round-1].mp3);

    audio.play();
}