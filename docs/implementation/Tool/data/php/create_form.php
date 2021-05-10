<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
   $titel = $_POST["antrag_titel"];
   $vorname = $_POST["antrag_vorname"];
   $nachname = $_POST["antrag_nachname"];
   $email = $_POST["antrag_email"];
   //$datum = $_POST["antrag_datum"];
   $text = $_POST["antrag_text"];
   $grund = $_POST["antrag_grund"];
   $vorschlag = $_POST["antrag_vorschlag"];
   $anlagen = $_POST["antrag_anlagen"];
   echo "$titel $vorname $nachname $email $text $grund $vorschlag $anlagen";

   exec("python /Users/ruben/Library/Mobile Documents/com~apple~CloudDocs/Documents/Uni Online/I3_Antragsverwaltungstool/docs/implementation/demo/files/python/create_form.py $titel $vorname $nachname $email $text $grund $vorschlag $anlagen", $output);
   print_r($output);
}
