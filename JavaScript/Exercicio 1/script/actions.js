

const userName = document.getElementById('i-name');
const birthDate = document.getElementById('i-birthDate');
const orders = document.getElementById('i-orders');
const submit = document.getElementById('i-submit');

// Divs
const container = document.getElementById('container');

submit.onclick = formSubmit;

function formSubmit() {
    const currentDate = new Date();
    let currentYear = currentDate.getFullYear();

    // Calcular a idade do usuário a partir do ano atual    

    console.log(userName.value);
    console.log(birthDate.value);
    console.log(orders.value);

    container.style.display = 'none';
}