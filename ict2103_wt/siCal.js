function sim_calculate () {
    let principal = document.getElementById('principal')
    let principalVal = parseFloat(principal.value)
    let rate = parseFloat(document.getElementById('rate').value)
    let time = parseFloat(document.getElementById('time').value)

    let si = (principalVal * rate * time)/100

    if (si >= 1000) {
        document.getElementById('result').style.color = "red"    
    } else {
        document.getElementById('result').style.color = "green"
    }

    document.getElementById('result').innerHTML = si
}