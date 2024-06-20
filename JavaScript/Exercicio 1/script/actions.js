

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


    delivery();
}


function delivery() {
    const deliverAt = document.getElementById('deliver-at');
    const productName = document.getElementById('product-name');
    const productValue = document.getElementById('product-value');
    const customerName = document.getElementById('customer-name');
    const currentDate = new Date();

    productsValues = {
        "macarrao" : "39.99 R$",
        "omelete" : "14.99 R$"
    }

    productsPrepTime = {
        "macarrao" : 2,
        "omelete" : 1
    }

    let deliverHour = (currentDate.getHours() + productsPrepTime[orders.value]) + ':' + currentDate.getMinutes();

    // Atualizar informações
    productName.textContent = orders.value;
    productValue.textContent = productsValues[orders.value];
    deliverAt.textContent = deliverHour;
    customerName.textContent = `Endereço: casa do(a) ${userName.value}`;
    

}