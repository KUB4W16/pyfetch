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
    description.innerHTML = '<p>pyfetch is an information tool such as <a class="link" href="https://github.com/KittyKatt/screenFetch">screenfetch</a> that we have on linux. It give you the python version, pip version, pip packages number, OS architecture. After runing the script you can choose one of three options: [1]Show packages list, [2]Find module description and [3]Exit. You can get a description of the modules from PyPi, a list of the packages and of course you can exit.</p>';
}
function openGithub() {
    location.href = "https://github.com/KUB4W16/pyfetch";
}
