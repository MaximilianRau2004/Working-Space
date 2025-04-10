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

/** 
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
*/

// calculator

function add(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("Both arguments must be numbers");
  }
  return a + b;
}

function sub(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("Both arguments must be numbers");
  }
  return a - b;
}

function mul(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("Both arguments must be numbers");
  }
  return a * b;
}

function div(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("Both arguments must be numbers");
  }
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

function mod(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("Both arguments must be numbers");
  }
  return a % b;
}

function pow(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("Both arguments must be numbers");
  }

  let c = a;
  for (let i = 1; i < b; i++) {
    a *= c;
  }
  return a;
}

function sqrt(a) {
  if (typeof a !== "number") {
    throw new TypeError("The argument must be a number");
  }
  return Math.sqrt(a);
}

function fac(a) {
  if (typeof a !== "number") {
    throw new TypeError("The argument must be a number");
  }
  for (let i = 1; i < a; i++) {
    a *= i;
  }
  return a;
}

// temperature converter

const textBox = document.getElementById("textBox");
const toFahrenheit = document.getElementById("toFahrenheit");
const toCelsius = document.getElementById("toCelsius");
const result = document.getElementById("result");
let temp;

function convert() {
  if (toFahrenheit.checked) {
    temp = Number(textBox.value);
    temp = temp * (9 / 5) + 32;
    result.textContent = temp.toFixed(1) + " °F";
  } else if (toCelsius.checked) {
    temp = Number(textBox.value);
    temp = (temp - 32) * (5 / 9);
    result.textContent = temp.toFixed(1) + " °C";
  } else {
    result.textContent = "Select an unit";
  }
}

// dice roller game

function rollDice() {
  const numOfDice = document.getElementById("numOfDice").value;
  const diceResult = document.getElementById("diceResult");
  const diceImages = document.getElementById("diceImages");
  const values = [];
  const images = [];

  for (let i = 0; i < numOfDice; i++) {
    const value = Math.floor(Math.random() * 6) + 1;
    values.push(value);
    images.push(`<img src="dice/${value}.svg" alt="Dice ${value}">`);
  }
  diceResult.textContent = `dice: ${values.join(", ")}`;
  diceImages.innerHTML = images.join("");
}

// random password generator

function generatePassword(
  length,
  includeLowercase,
  includeUppercase,
  includeNumbers,
  includeSymbols
) {
  const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
  const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const numberChars = "0123456789";
  const symbolChars = "!@#$%^&*()_+[]{}|;:,.<>?";

  let allowedChars = "";
  let password = "";

  allowedChars += includeLowercase ? lowercaseChars : "";
  allowedChars += includeUppercase ? uppercaseChars : "";
  allowedChars += includeNumbers ? numberChars : "";
  allowedChars += includeSymbols ? symbolChars : "";

  if (length <= 0) {
    return "Password length must be greater than 0.";
  }

  if (allowedChars.length === 0) {
    return "At least one character type must be selected.";
  }

  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * allowedChars.length);
    password += allowedChars[randomIndex];
  }

  return password;
}

const passwordLength = 12;
const includeLowercase = true;
const includeUppercase = true;
const includeNumbers = true;
const includeSymbols = true;

const password = generatePassword(
  passwordLength,
  includeLowercase,
  includeUppercase,
  includeNumbers,
  includeSymbols
);

console.log(`Generated password: ${password}`);

const person1 = {
  firstName: "Spongebob",
  lastName: "Squarepants",
  age: 20,
  isEmployed: true,
  sayHello: function () {
    console.log(`Hello, my name is ${this.firstName} ${this.lastName}`);
  },
};

const person2 = {
  firstName: "Patrick",
  lastName: "Star",
  age: 20,
  isEmployed: false,
};

person1.sayHello();

function Car(make, model, year, color) {
  this.make = make;
  this.model = model;
  this.year = year;
  this.color = color;
  this.start = function () {
    console.log(`Starting ${this.make} ${this.model}`);
  };
}

const car1 = new Car("Toyota", "Camry", 2020, "blue");
const car2 = new Car("Honda", "Civic", 2021, "red");
const car3 = new Car("Ford", "Mustang", 2022, "black");

car1.start;

class Product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
  getInfo() {
    console.log(`${this.name} costs $${this.price}`);
  }

  calculateTotal(salesTax) {
    return this.price + this.price * salesTax;
  }
}

const salesTax = 0.05;

const product1 = new Product("Laptop", 999.99);
const product2 = new Product("Smartphone", 699.99);

product1.getInfo();

const total = product1.calculateTotal(salesTax);
console.log(`Total price with tax: $${total.toFixed(2)}`);

class MathUtil {
  static PI = 3.14159;

  static getDiameter(radius) {
    return radius * 2;
  }
  static getCircumference(radius) {
    return radius * 2 * this.PI;
  }
}

console.log(`Diameter of a circle with radius 5: ${MathUtil.getDiameter(5)}`);
console.log(
  `Circumference of a circle with radius 5: ${MathUtil.getCircumference(5)}`
);

class User {
  static userCount = 0;

  constructor(username) {
    this.username = username;
    User.userCount++;
  }

  static getUserCount() {
    console.log(`Total users: ${User.userCount}`);
  }

  sayHello() {
    console.log(`Hello, my name is ${this.username}`);
  }
}

const user1 = new User("Alice");
const user2 = new User("Bob");
const user3 = new User("Charlie");

user1.sayHello();
User.getUserCount();

class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  move() {
    console.log(`${this.name} is moving`);
  }
}

class Rabbit extends Animal {
  constructor(name, age, runSpeed) {
    super(name, age);
    this.runSpeed = runSpeed;
  }

  run() {
    console.log(`${this.name} is running at ${this.runSpeed} km/h`);
    super.move();
  }
}

class Fish extends Animal {
  constructor(name, age, swimSpeed) {
    super(name, age);
    this.swimSpeed = swimSpeed;
  }
}

class Hawk extends Animal {
  constructor(name, age, flySpeed) {
    super(name, age);
    this.flySpeed = flySpeed;
  }
}

const rabbit = new Rabbit("Bunny", 2, 30);
const fish = new Fish("Nemo", 1, 10);
const hawk = new Hawk("Hawky", 3, 50);

rabbit.run();


class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  set width(width) {
    if (width <= 0) {
      throw new Error("Width must be greater than 0.");
    }
    this._width = width;
  }

  set height(height) {
    if (height <= 0) {
      throw new Error("Height must be greater than 0.");
    }
    this._height = height;
  }

  get width() {
    return this._width.toFixed(1);
  }
  get height() {
    return this._height.toFixed(1);
  }

  get area() {
    return (this._width * this._height).toFixed(1);
  }

}

const rectangle = new Rectangle(5, 10);

rectangle.width = 15; 
rectangle.height = 20; 

console.log(rectangle.width); 
console.log(rectangle.height); 
console.log(rectangle.area);


const deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'];

function shuffleDeck(deck) {
  for (let i = deck.length - 1; i > 0; i--) {
       const random = Math.floor(Math.random() * (i + 1));

       [deck[i], deck[random]] = [deck[random], deck[i]];
  }
}

shuffleDeck(deck);

console.log(deck);


const date = new Date(1);

console.log(date);
