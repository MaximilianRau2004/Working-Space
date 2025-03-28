// counter

const incrementBtn = document.getElementById("incrementButton");
const decrementBtn = document.getElementById("decrementButton");
const resetBtn = document.getElementById("resetButton");
const countLabel = document.getElementById("countLabel");
let count = 0;

incrementBtn.onclick = function () {
  count++;
  countLabel.textContent = count;
};

decrementBtn.onclick = function () {
  count--;
  countLabel.textContent = count;
};

resetBtn.onclick = function () {
  count = 0;
  countLabel.textContent = count;
};

// random number generator

const myButton = document.getElementById("myButton");
const label1 = document.getElementById("label1");
const label2 = document.getElementById("label2");
const label3 = document.getElementById("label3");
const min = 1;
const max = 6;
let randomNum1;
let randomNum2;
let randomNum3;

myButton.onclick = function () {
  randomNum1 = Math.floor(Math.random() * max) + min;
  randomNum2 = Math.floor(Math.random() * max) + min;
  randomNum3 = Math.floor(Math.random() * max) + min;
  label1.textContent = randomNum1;
  label2.textContent = randomNum2;
  label3.textContent = randomNum3;
};

// age checker

const myText = document.getElementById("myText");
const myButton2 = document.getElementById("myButton2");
const resultElement = document.getElementById("resultElement");

myButton2.onclick = function () {
  let age = myText.value.trim();
  age = Number(age);

  if (isNaN(age)) {
    resultElement.textContent = "Please enter a valid number.";
  } else if (age >= 100) {
    resultElement.textContent = "You are too old.";
  } else if (age >= 18) {
    resultElement.textContent = "You are an adult.";
  } else if (age === 0) {
    resultElement.textContent = "You were just born.";
  } else if (age < 0) {
    resultElement.textContent = "You are not born yet.";
  } else {
    resultElement.textContent = "You are a child.";
  }
};

// checkbox

const myCheckbox = document.getElementById("myCheckbox");
const visaBtn = document.getElementById("visaBtn");
const masterCardBtn = document.getElementById("masterCardBtn");
const payPalBtn = document.getElementById("payPalBtn");
const myButton3 = document.getElementById("myButton3");
const subResult = document.getElementById("subResult");
const PaymentResult = document.getElementById("paymentResult");

myButton3.onclick = function () {
  if (myCheckbox.checked) {
    subResult.textContent = "You are subsribed";
  } else {
    subResult.textContent = "You are not subsribed";
  }

  if (visaBtn.checked) {
    PaymentResult.textContent = "You have selected Visa";
  } else if (masterCardBtn.checked) {
    PaymentResult.textContent = "You have selected MasterCard";
  } else if (payPalBtn.checked) {
    PaymentResult.textContent = "You have selected PayPal";
  } else {
    PaymentResult.textContent = "Please select a payment method";
  }
};

// ternär: condition ? exprIfTrue : exprIfFalse

/** 
 * switch
let testScore = 92;
let letterGrade;

switch (true) {
  case testScore >= 90:
    letterGrade = "A";
    break;
  case testScore >= 80:
    letterGrade = "B";
    break;
  case testScore >= 70:
    letterGrade = "C";
    break;
  case testScore >= 60:
    letterGrade = "D";
    break;
   default:
    letterGrade = "F";   
}
 
console.log(letterGrade);
*/

// Number guessing game

const minNum = 1;
const maxNum = 100;
const randomNum = Math.floor(Math.random() * maxNum) + minNum;

let attempts = 0;
let guess;
let running = true;

while (running) {
  guess = prompt(`Enter a number between ${minNum} and ${maxNum}`);
  guess = Number(guess);

  if (isNaN(guess)) {
    alert("Please enter a valid number.");
  } else if (guess < minNum || guess > maxNum) {
    alert(`Please enter a number between ${minNum} and ${maxNum}`);
  } else {
    attempts++;
    if (guess < randomNum) {
      alert("Too low! try again.");
    } else if (guess > randomNum) {
      alert("Too high! try again.");
    } else {
      alert(`Congratulations! You guessed the number ${randomNum} in ${attempts} attempts.`);
      running = false;
    }
  }
}

