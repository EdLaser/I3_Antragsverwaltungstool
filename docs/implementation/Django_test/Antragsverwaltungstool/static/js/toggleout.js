function toggleout(f) {

    var x = document.getElementById(f);
    if (x.style.visibility === "hidden") {
        x.style.visibility = "visible";
    }else{
        x.style.visibility = "hidden";
    }
}