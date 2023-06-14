// Remove alert
function removeFlash() {
    const element = document.getElementById('alert');
    element.remove();
}
  
// Open sidebar
function openSidebar() {
    var element = document.getElementById('sidebar');
    var backgroundBlock = document.getElementById('background-block');
    let pos = 0;
    let id = null;
    element.style.display = "block";
    let op = 0;
    clearInterval(id);
    id = setInterval(frame, 1);
    function frame() {
        if (pos == 250) {
            clearInterval(id);
        }
        else {
            pos += 10;
            element.style.left = pos - 250 + "px";
            op += 0.01;
            backgroundBlock.style.opacity = op;
            backgroundBlock.style.display = "block";
        }
    }
}
  
// Close sidebar
function closeSidebar() {
    var element = document.getElementById('sidebar');
    var backgroundBlock = document.getElementById('background-block');
    let pos = 0;
    let id = null;
    let op = 0.25;
    clearInterval(id);
    id = setInterval(frame, 1);
    function frame() {
        if (pos == -250) {
            clearInterval(id);
            backgroundBlock.style.display = "none";
        }
        else {
            pos-= 10;
            element.style.left = pos + "px";
            op -= 0.01;
            backgroundBlock.style.opacity = op;
        }
    }
}