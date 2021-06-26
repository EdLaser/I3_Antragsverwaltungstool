function toggledisplay(f){
    var x = document.getElementById(f);
    var Sin = document.getElementById("Sin").value;     //Stellen Input
    if(Sin === "18") {
        if (x.style.display === "none") {
            x.style.display = "block";
        }
    }else {
        x.style.display = "none";
    }
}