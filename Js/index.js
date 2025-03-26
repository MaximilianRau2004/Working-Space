// counter

const incrementBtn = document.getElementById('incrementButton');
const decrementBtn = document.getElementById('decrementButton');
const resetBtn = document.getElementById('resetButton');
const countLabel = document.getElementById('countLabel');
let count = 0;

incrementBtn.onclick = function() {
    count++;
    countLabel.textContent = count;
}

decrementBtn.onclick = function() {
    count--;
    countLabel.textContent = count;
}

resetBtn.onclick = function() {
    count = 0;
    countLabel.textContent = count;
}

// random number generator

const myButton = document.getElementById('myButton');
const label1 = document.getElementById('label1');
const label2 = document.getElementById('label2');
const label3 = document.getElementById('label3');
const min = 1;
const max = 6;
let randomNum1;
let randomNum2;
let randomNum3;

myButton.onclick = function() {
    randomNum1 = Math.floor(Math.random() * max) + min;
    randomNum2 = Math.floor(Math.random() * max) + min;
    randomNum3 = Math.floor(Math.random() * max) + min;
    label1.textContent = randomNum1;
    label2.textContent = randomNum2;
    label3.textContent = randomNum3;
}

// age checker

const myText = document.getElementById('myText');
const mySubmit = document.getElementById('mySubmit');
const resultElement = document.getElementById('resultElement');
let age;

mySubmit.onclick = function() {
    age = myText.value;
    age = Number(age);
    if (age >= 100) {
        resultElement.textContent = 'You are too old.';
    } else if (age >= 18) {
        resultElement.textContent = 'You are an adult';
    } else if (age == 0) {
        resultElement.textContent = 'You were just born';
    } else if (age < 0) {
        resultElement.textContent = 'You are not born yet';
    }
    else {
        resultElement.textContent = 'You are a child';
    }
}
