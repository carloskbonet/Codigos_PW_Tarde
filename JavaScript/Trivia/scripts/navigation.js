const startButton = document.getElementById('start');
const configsButton = document.getElementById('configs');
const optionsMenu = document.getElementById('options');
var timeToAnswer = 15;


configsButton.onclick = openOptions
startButton.onclick = startGame;


function startGame() {
    window.location.replace(`./gameplay.html?time=${timeToAnswer}`);

    //http://127.0.0.1:5500/Codigos_PW_Tarde/JavaScript/Trivia/html/index.html

    //http://127.0.0.1:5500/Codigos_PW_Tarde/JavaScript/Trivia/html/gameplay.html?time=15
}


function openOptions() {
    if ( optionsMenu.style.display == 'none' ) {
        optionsMenu.style.display = 'block';
    }
    else {
        optionsMenu.style.display = 'none';
    }
}

function chooseDif(time) {
    timeToAnswer = time;
    
    alert(`Tempo definido para responder cada questão: ${time} segundos`);
}