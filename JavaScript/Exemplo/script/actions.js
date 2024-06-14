
//console.log('Hello World');

var nome = "";
var idade = 0;
const birthYear = document.getElementById('i-birthYear');
const Response = document.getElementById('response');

function saudacao() {
    idade = 2024 - birthYear.value;
    console.log(idade);

    if ( idade >= 18 ){
        console.log('Você pode ter CNH');

        Response.textContent = 'Você pode ter CNH';

        alert('Você pode ter CNH')
    }
    else {
        console.log('Espere mais um pouco, você ainda não pode ter CNH ☹️☠️😎🤯');
        console.log(`Faltam ${18 - idade} anos para fazer 18 anos`);

        Response.textContent = `Espere mais um pouco, você ainda não pode ter CNH ☹️☠️😎🤯` + 
        `Faltam ${18 - idade} anos para fazer 18 anos`;
    }

}