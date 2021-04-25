
$('#antrag_submit').addEventListener('click', function ()
{
    if(confirm('Antrag stellen ?')) {
        let antragTitel = $('#antrag_titel').value;
        let antragVorname = $('#antrag_vorname').value;
        let antagNachname = $('#antrag_nachname').value;
        let antragEmail = $('#antrag_email').value;
        let antragDatum = $('#antrag_datum').value;
        let antragText = $('#antrag_text').value;
        let antragGrund = $('#antrag_grund').value;
        let antragVorschlag = $('#antrag_vorschlag').value;
        let antragAnlagen = $('#antrag_anlagen').value;



    } else {
        return;
    }

})