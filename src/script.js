document.addEventListener("keypress", function(event){
    if (event.keyCode == 49){
        home()
    }
    else if (event.keyCode == 50){
        about()
    }
    else if (event.keyCode == 51){
        openGithub()
    }
})

function home(){
    document.getElementById("text").innerHTML = "<p>pyfetch - information tool like linux screenfetch</p>";
}
function about(){
    document.getElementById("text").innerHTML = '<p>pyfetch is information tool like <a class="link" href="https://github.com/KittyKatt/screenFetch">screenfetch</a> we can see on linux. If you run this script, remember to run script in cmd not in python shell. It give you python version, pip version, pip packages number, OS and architecture.</p>';
}
function openGithub(){
    location.href = "https://github.com/KUB4W16/pyfetch";
}