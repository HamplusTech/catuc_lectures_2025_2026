document.getElementById('proceed').onclick = function(){
    let nameDB = []
    let numberDB = []

    if (localStorage.getItem('NAME') != null) {
        nameDB.push(localStorage.getItem('NAME'))
    }

    if (localStorage.getItem('NUMBER') != null) {
        numberDB.push(localStorage.getItem('NUMBER'))
    }

    let candName = document.getElementById('candName')
    let candNumber = document.getElementById('candNumber')
    if (candName.value == "" & candNumber.value == "") {
        alert("You must fill the Candidate's details")
        } else if (candName.value == "") {
        alert("You must fill the Candidate's name")
    } else if (candNumber.value == ""){
        alert("You must fill the Candidate's exam number")
    } else if (candNumber.value.length > 4) {
        alert ("Candidate's exam number can't be more than 4 digits")
    } else {
        document.getElementById('exam').removeAttribute('hidden')
        document.getElementById('login').setAttribute("hidden", true)

        nameDB.push(candName.value)
        numberDB.push(candNumber.value)

        localStorage.setItem("NAME", nameDB)
        localStorage.setItem("NUMBER", numberDB)
    }
}

document.getElementById('goBack').onclick = function(){
    document.getElementById('exam').setAttribute("hidden", true)
    document.getElementById('login').removeAttribute('hidden')
}

document.getElementById('submit').onclick = function() {
    let questNumber = document.querySelectorAll("li h3")

    let answers = []

    for (let a = 1; a <= questNumber.length; a += 1) {
        let tagName = `quest${a}`
        let optTag = document.getElementsByName(tagName)
        optTag.forEach(opt => {
            if (opt.checked) {
                answers.push(opt.value)
            }
        });
    }

    let sumAnswers = 0
    answers.forEach(element => {
        sumAnswers += parseInt(element)
    });

    let scoreDB = []

    if (localStorage.getItem('SCORE') != null) {
        scoreDB.push(localStorage.getItem('SCORE'))
    }

    scoreDB.push(sumAnswers)

    localStorage.setItem("SCORE", scoreDB)
}