const startButton = document.getElementById('start');
const configsButton = document.getElementById('configs');
const optionsMenu = document.getElementById('options');


configsButton.onclick = openOptions
startButton.onclick = startGame;


function startGame() {
    window.location.replace('./gameplay.html')

    //http://127.0.0.1:5500/Codigos_PW_Tarde/JavaScript/Trivia/html/index.html
}


function openOptions() {
    if ( optionsMenu.style.display == 'none' ) {
        optionsMenu.style.display = 'block';
    }
    else {
        optionsMenu.style.display = 'none';
    }
}