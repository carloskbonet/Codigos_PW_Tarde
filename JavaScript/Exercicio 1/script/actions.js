

const userName = document.getElementById('i-name');
const birthDate = document.getElementById('i-birthDate');
const orders = document.getElementById('i-orders');
const submit = document.getElementById('i-submit');

submit.onclick = formSubmit;

function formSubmit() {
    console.log(userName.value);
    console.log(birthDate.value);
    console.log(orders.value);
}