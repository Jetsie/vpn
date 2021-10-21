var elem = document.documentElement;
let tabBar = document.getElementById("tabBar");
let urlBar = document.getElementById("urlBar");

function EnterApp() {
    if (document.exitFullscreen) {
    document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
    document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
    document.msExitFullscreen();
    }
    tabBar.style.display="block";
    urlBar.style.display="block";
}

function ExitApp() {
    if (document.exitFullscreen) {
    document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
    document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
    document.msExitFullscreen();
    }
    tabBar.style.display="none";
    urlBar.style.display="none";
}

function toggle(button) {
    if (button.value == "App Mode") {
        button.value = "Web Mode";
        EnterApp();
        
    } else {
        button.value = "App Mode";
        ExitApp();
    }
}

ExitApp();