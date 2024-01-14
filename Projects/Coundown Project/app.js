const End_date = prompt("Enter Your last Date ", "")
document.getElementById("Endtime").innerHTML = End_date
const inputs = document.querySelectorAll("input");

function clock() {
    const end = new Date(End_date)
    const now = new Date();
    const diff = (end - now) / 1000;
    if (diff < 0) {
        return
    }
    //convetring to hours

    inputs[0].value = Math.floor(diff / 3600 / 24)
    inputs[1].value = Math.floor(diff / 3600) % 24
    inputs[2].value = Math.floor(diff / 60) % 60
    inputs[3].value = Math.floor(diff) % 60
}

clock();

setInterval(() => {
    clock()
}, 1000)