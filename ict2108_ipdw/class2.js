var age; 
let names_student = "Kelly"; // string
age = 24; // number
// alert(typeof(age))
// console.log(typeof(age))
// document.writeln(typeof(names_student))
let students_name = ["Jude", "Gordon", "Achily", "Sonia"]
document.writeln(typeof(students_name))
console.log(typeof(students_name))
console.log(students_name)
let data = Array(23, "Catuc", [45, 67])
console.log(data)
let stud_data = {
    "name" : ["Jude", "Gordon", "Achily", "Sonia"],
    "score" : [20, 10, 20, 10]
}

console.log(data[1])

// console.log(data[2][1])

stud_data["name"].forEach(data => console.log(data))

for (let i=0; i < stud_data["name"].length; i += 1) {
    console.log(stud_data["name"][i] + " scored " + stud_data["score"][i])
}

console.log("Another method")

// Object.keys(stud_data).forEach((key, value) => {
//     console. log(`${key} scored ${value}`)
// })
