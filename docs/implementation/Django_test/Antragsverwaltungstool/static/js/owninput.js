function mytoggleinputs(f) {

    var Sin = document.getElementById("Sin").value;     //Stellen Input
    var x = document.getElementById(f);
    if(Sin === "18") {
        if (x.style.visibility === "hidden") {
            x.style.visibility = "visible";
        }
    } else {
        x.style.visibility = "hidden";
    }
}