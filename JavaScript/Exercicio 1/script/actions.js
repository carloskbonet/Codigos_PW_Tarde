

const userName = document.getElementById('i-name');
const birthDate = document.getElementById('i-birthDate');
const orders = document.getElementById('i-orders');
const submit = document.getElementById('i-submit');

// Divs
const container = document.getElementById('container');
const container2 = document.getElementById('container-2');

submit.onclick = formSubmit;

function formSubmit() {
    
    const currentDate = new Date();
    let currentYear = currentDate.getFullYear();
    let currentMonth = currentDate.getMonth() + 1;
    let currentDay = currentDate.getDate();

    let stringDate = `${currentYear}-${currentMonth}-${currentDay}`;
    let dateMin = `${currentYear - 100}-${currentMonth}-${currentDay}`;
    let dateMax = `${currentYear - 16}-${currentMonth}-${currentDay}`;

    // Calcular a idade do usuário a partir do ano atual    

    // Validar o tamanho do nome. Tamanho mínimo e máximo.
    // and  &&
    // or   ||
    if ( userName.value.length < 3 || userName.value.length > 16) {
        alert('O nome deve conter de 3 a 16 letras.');
        return;
    }

    // Validar a data de nascimento. Valor mínimo e máximo.
    if ( birthDate.value < dateMin || birthDate.value > dateMax ) {
        alert('Data de nascimento inválida. Coloque um ano entre 1924 e 2008');
        return;
    }

    console.log(userName.value);
    console.log(birthDate.value);
    console.log(orders.value);

    container.style.display = 'none';

    container2.style.display = 'block';
}

//  Container 2 ( Interface de Status da compra )

// Icone da Loja / Nome ao lado do icone

// Mensagem de "Pedido concluído"

// Produto selecionado para a compra

// Valor do produto (Possível cupom)

// Horário previsto para a entrega