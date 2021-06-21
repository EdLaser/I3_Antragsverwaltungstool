function questiontoggel(){
    var x = document.getElementById("frg");
    if(document.getElementById('Fin').checked === true) {
        x.style.display = "none";
    }else {
        x.style.display = "block";
    }
}