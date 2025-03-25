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