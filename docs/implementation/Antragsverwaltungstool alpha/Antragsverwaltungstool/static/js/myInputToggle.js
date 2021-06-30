function questiontoggel(){
    var x = document.getElementById("frg");
    if(document.getElementById('Fin').checked === true) {
        x.style.display = "none";
    }else {
        x.style.display = "block";
    }
}

function togglecheck(toggleID1,radioID){
    var x = document.getElementById(toggleID1);
    if(document.getElementById(radioID).checked === true) {
        x.style.display = "none";
    }else {
        x.style.display = "block";
    }
}

function togglecheck_stura(toggleID1,toggleID2,radioID){
    var x = document.getElementById(toggleID1);
    var y = document.getElementById(toggleID2);
    if(document.getElementById(radioID).checked === true) {
        x.style.display = "none";
        y.style.display = "block";
    }else {
        x.style.display = "block";
        y.style.display = "none";
    }
}

function toggleout(f) {

    var x = document.getElementById(f);
    if (x.style.visibility === "hidden") {
        x.style.visibility = "visible";
    }else{
        x.style.visibility = "hidden";
    }
}

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