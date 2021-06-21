function setdate() {
    var currentdate = new Date();
    var year = currentdate.getFullYear();
    var month = currentdate.getMonth()+1;
    var day = currentdate.getDay();

    if(month < 10){
        month = "0" + month;
    }

    if(day < 10){
        day = "0" + day;
    }

    var today = day + "." + month + "." + year;

    document.getElementById('mydate').innerHTML = (today);
}