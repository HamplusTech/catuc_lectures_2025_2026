function tossCoin() {
    let coin1 = ['H', 'T']
    let coin2 = ['H', 'T']

    let result = (coin1[Math.round(Math.random(coin1.length))]) + (coin2[Math.round(Math.random(coin1.length))]);

    return (result);
}

// console.log(tossCoin())

function gameResult() {
    let comGuess = tossCoin();
    let userGuess = document.getElementById('userGuess').value;

    document.getElementById('userResult').innerHTML = userGuess;

    document.getElementById('comResult').innerHTML = comGuess;

    if (parseFloat(userGuess)) {
        document.getElementById('finalResult').innerHTML = "Ooops! You entered a number. Please enter a string!!!<br>Try Again.<br><br>Thanks."

        document.getElementById('finalResult').style.backgroundColor = "red"

        document.getElementById('finalResult').style.color = "pink"
    } else {
        if (comGuess == userGuess) {
            document.getElementById('finalResult').innerHTML = "Congrats! You won!!! <br><br>Thanks."

            document.getElementById('finalResult').style.backgroundColor = "Green"

            document.getElementById('finalResult').style.color = "white"
        } else {
            document.getElementById('finalResult').innerHTML = "Ooops! You Failed!!!<br>Try Again.<br><br>Thanks."

            document.getElementById('finalResult').style.backgroundColor = "red"

            document.getElementById('finalResult').style.color = "pink"
        }
    }

}

function capital(a) {
    setTimeout(function () {
        a.value = a.value.toUpperCase();
    }, 1);
}