function toggledisplay(f){
    var x = document.getElementById(f);
    if(x.style.display === "none") {
        x.style.display = "block";
    }else {
        x.style.display = "none";
    }
}