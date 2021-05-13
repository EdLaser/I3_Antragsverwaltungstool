<?php
    $titel = "Testantrag";
    $fname = $_POST["fname"];
    $lname = $_POST["lname"];
    $email = "ruben@kraus.de";
    $datum = "10.05.2021";
    $antrtext= $_POST["antrtext"];
    $frg1 = $_POST["frg1"];
    $frg2 = $_POST["frg2"];
    $frg3 = $_POST["frg3"];
    $frg4 = $_POST["frg4"];
    echo "$titel $fname $lname $email $antrtext $frg1 $frg2 $frg3 $frg4";

    $command = "python /Users/ruben/Documents/SE/I3_Antragsverwaltungstool/docs/implementation/Tool/data/python/insert_form.py";
    exec("$command $titel $fname $lname $email $antrtext $frg1 $frg2 $frg3 $frg4", $output);
    print_r( $output);
?>