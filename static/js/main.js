var elem = document.documentElement;

function openFullscreen() {
    if (elem.requestFullscreen) {
    elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
    elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
    elem.msRequestFullscreen();
    }
}

function closeFullscreen() {
    if (document.exitFullscreen) {
    document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
    document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
    document.msExitFullscreen();
    }
}

function EnterApp() {
    openFullscreen();
    tabBar.style.display="block";
    urlBar.style.display="block";
}

function ExitApp() {
    closeFullscreen();
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