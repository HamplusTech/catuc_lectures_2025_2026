function register() {
    let fname = document.getElementById('fname').value
    let uname = document.getElementById('uname').value
    let pword = document.getElementById('pword').value
    let dob = document.getElementById('dob').value
    let pnumber = document.getElementById('pnumber').value
    let eaddress = document.getElementById('eaddress').value
    let gender = document.getElementById('gender').value
    
    // document.cookie = fname
    let data = localStorage.getItem("fname")
    data = [data]
    data.push(fname)
    localStorage.setItem("fname", data)

    // document.getElementById("clear").addEventListener('click', function(){
        document.getElementById("fname").value = ""
    // })

    alert("Registration Successuly")
}