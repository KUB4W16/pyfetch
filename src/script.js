document.addEventListener("keypress", function (event) {
    if (event.keyCode == 49) {
        home()
    }
    else if (event.keyCode == 50) {
        about()
    }
    else if (event.keyCode == 51) {
        openGithub()
    }
})

var description = document.getElementById("description");

function home() {
    description.innerHTML = "<p>pyfetch - information tool like linux screenfetch</p>";
}
function about() {
    description.innerHTML = '<p>pyfetch is information tool like <a class="link" href="https://github.com/KittyKatt/screenFetch">screenfetch</a> we can see on linux. If you run this script, remember to run script in cmd not in python shell. It give you python version, pip version, pip packages number, OS and architecture. If you run script you can choose one of three options: [1]Show packages list, [2]Find module description and [3]Exit. You can get description of modules from PyPi, list of packages and of course you can exit.</p>';
}
function openGithub() {
    location.href = "https://github.com/KUB4W16/pyfetch";
}
