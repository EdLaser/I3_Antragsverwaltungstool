/*dropArea.addEventListener('dragover', (event) => {
    //Prevent Browser from default actions -> dont open files in new window
    event.stopPropagation();
    event.preventDefault();

    event.dataTransfer.dropEffect = 'copy';
});*/
/*dropArea.addEventListener('drop', (event) => {
    event.stopPropagation();
    event.preventDefault();
    const fileList = event.dataTransfer.files; //Get file list
    console.log(fileList);                     //Print file log
});*/
//dropArea.addEventListener('drop', (event) => { ...
// equals: dropArea.addEventlistener('drop', function(event) { ...
/*function readFile(file) {
    //Check if file is not pdf
    if (file.type && !file.type.startsWith('pdf/')) {
        console.log(file, 'Is not supported');
        return;
    }

    const reader = new FileReader();
    reader.addEventListener('load',(event)=> {
        file.src = event.target.result;
        reader.readAsText(file);
    });
}*/
/*function readFile() {
    let reader = new FileReader();
    reader.addEventListener('load', function (event) {
        let text = event.target.result;
        document.getElementById('output').textContent = text;
    });
}
const fileArea = document.getElementById('#filezone');
fileArea.addEventListener('change', readFile);*/

document.getElementById('filezone').addEventListener('change',function fileSelected(){
    console.log(this.files);
    let file = this.files[0];

    if ( file.size===0) {
        console.log('No file');
        return
    }
    let reader = new FileReader();
    reader.onload = function (progressEvent) {
        console.log(reader.result);
    };
    document.getElementById('out').innerHTML = this.files;
});