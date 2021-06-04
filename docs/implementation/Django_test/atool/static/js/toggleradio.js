function toggleradio(toggleID,radioID){
    var x = document.getElementById(toggleID);
    if(document.getElementById(radioID).checked === true) {
        x.style.display = "none";
    }else {
        x.style.display = "block";
    }
}