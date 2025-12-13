function addNumbers() {
    let firstNumber = 12
    let secondNumber = 11;
    return document.getElementById('result').innerHTML = firstNumber + secondNumber
    // return document.getElementById('result2').value = firstNumber + secondNumber
}

function addNumbersP(first, second) {
    return first + second
}

let res = addNumbersP(34, 11)
// document.getElementById('result2').innerHTML = res

console.log(addNumbersP(200, 500))

function fc(){
    let colourTag = document.getElementById('fc')
    let colourValue = colourTag.value

    document.getElementById('setting').style.color = colourValue

    let bgTag = document.getElementById('bgc')
    let bgValue = bgTag.value

    document.getElementById('setting').style.backgroundColor = bgValue
} 

document.getElementById('colorNew').addEventListener('change', function() {
    document.getElementById('setting').style.color = document.getElementById('colorNew').value
});

document.getElementById('colorNew2').addEventListener('change', function() {
    document.getElementById('setting').style.backgroundColor = this.value
});