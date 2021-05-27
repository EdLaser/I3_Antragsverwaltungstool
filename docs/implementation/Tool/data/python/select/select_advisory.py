#!/usr/bin/python3
import pymysql

# Establish connection
connect = pymysql.connect(host='192.168.19.129', user='ruben', password='1234', database='Antraege')

with connect:
    with connect.cursor() as cursor:
        statement = "SELECT * FROM advisory_member WHERE number = '2021-01-01'"
        cursor.execute(statement)
        result = cursor.fetchall()
        print(result)

html = """
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Antragverwaltungstool</title>
    <link rel="icon" href="icon.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="data/css/mainstyle.css">
    <link rel="stylesheet" href="data/css/W3.css">
    <link rel="stylesheet" href="data/css/intern.css">
    <link rel="stylesheet" href="data/css/login_popup.css">
    <script src="data/js/owninput.js"></script>
    <script src="data/js/toggleout.js"></script>
    <script src="data/js/toggledisplay.js"></script>
</head>
<body>
<div class = "logo w3-animate-top">
    <a href="index.html" class = "w3-hover-opacity"><img src="img/logo.png" class = "sturalogo" alt="ToolLogo"/></a>
</div>
<div class = "navigation">
    <ul class = "mainnav">
        <li class = "lil"><a href="index.html">Home</a></li>
        <li class = "lil"><a href="universally.html">Antrag ohne finanzielle Mittel</a></li>
        <li class = "dropdown lil"><a href="javascript:void(0)" class = "dropbtn">Antrag Wahl ▼</a>
            <div class = "dropdown-content w3-animate-opacity">
                <a href="advisory_member.html">Beratendes Mitglied</a>
                <a href="election_report.html">Stelle/Amt</a>
                <a href="#">Studienkomission</a>
            </div>
        </li>
        <li class = "lil"><a href="finance.html">Antrag mit finanziellen Mitteln</a></li>
        <li class = "lil"  id = "active" ><a href="intern.html">Intern</a></li>
        <li class = "lil"><a href="admin.html">Admin</a></li>

        <li class = "lir"><a href="https://www.stura.htw-dresden.de/">
            <img src="img/Stura_htw.png" style="width: 84px" alt = "SturaLogo"/></a>
        </li>
        <li class = "lir dropdown"><a class="dropbtn">
            <img src="img/login.png" style="width: 19px" alt = "login"/> Login</a>
            <div class = "dropdown-content w3-animate-opacity" id = "myLogin">
                <form class = "form-container" action="data/php/login.php" method="post">
                    <label><b>Rollenwahl</b></label>
                    <select class="w3-select w3-border" name = "role" required>
                        <option disabled selected>Bitte Auswählen</option>
                        <option name = "admin" value = "1">Admin</option>
                        <option name = "write" value = "2">Schriftführer</option>
                        <option name = "read" value = "3">Mitglied</option>
                    </select>
                    <label><b>Passwort</b></label>
                    <input type = "password" aria-placeholder="Passwort eingeben" name = "pwd" required>
                    <button type="submit" class = "btn w3-green">Login</button>
                </form>
            </div>
        </li>
    </ul>
</div>

<div class = "content w3-animate-opacity">
    <div class = "w3-row" style="margin-bottom: 20px">
        <div class="w3-half" style="width: 40%">
            <div class="w3-card-4" style="margin-right: 10px">
                <header class="w3-container" style="background-color: #F2AC2E;">
                    <h2>Referat wählen:</h2>
                </header>

                <div class="w3-container w3-light-gray">
                    <form class = "myform" action="data/php/intern.php">
                        <select class="w3-select w3-border form" id = "Sin" onchange="mytoggleinputs('oth')" name = "election_input" required>
                            <option disabled selected>Bitte Auswählen</option>
                            <option name = "pres" value = "1">Präsidium</option>
                            <option name = "ple" value = "2">Plenum</option>
                            <option name = "qm" value = "3">Quallitätsmanagement</option>
                            <option name = "tes" value = "4">Testreferat</option>
                            <option name = "other" value = "5">Eigene...</option>
                        </select>

                        <div id="oth" style = "visibility: hidden">
                            <label><b>Eigene:</b></label>
                            <input class = "w3-input w3-border form" placeholder="Beispielreferat" name = "owninput" ><br>
                        </div>
                    </form>
                </div>

                <footer class="w3-container w3-light-gray">
                    <input type="submit" class = "w3-button w3-green mybutton" value="Absenden" onclick="toggleout('out'),toggledisplay('applications')">
                </footer>
            </div>
        </div>

        <div class="w3-half" style="width: 60%; visibility: hidden" id = "out">
            <div class="w3-card-4">
                <header class="w3-container" style="background-color: #F2AC2E;">
                    <h2>Ausgabe:</h2>
                </header>

                <div class="w3-container w3-light-gray">
                    <div class = "sqloutput">

                    </div>
                </div>
            </div>
        </div>
    </div>

    <div style="display: none; margin-right: 10%; margin-left: 10%" id = "applications">
        <h1>Antragsart wählen:</h1>
        <table>
            <tr>
                <td><a href="universally_stura.html">
                    <img src="img/applications.png" class = "applimg" alt="Antagslogo"/><b>Antrag ohne finanzielle Mittel</b>
                </a></td>
                <td><a href="finance_stura.html">
                    <img src="img/applications.png" class = "applimg" alt="Antagslogo"/><b>Antrag mit finanziellen Mitteln</b>
                </a></td>
                <td><a href="advisory_member_stura.html">
                    <img src="img/applications.png" class = "applimg" alt="Antagslogo"/><b>Wahl Beratendes Mitglied</b>
                </a></td>
                <td><a href="election_report_stura.html">
                    <img src="img/applications.png" class = "applimg" alt="Antagslogo"/><b>Wahl auf Stelle/Amt</b>
                </a></td>
                <td><a href="#">
                    <img src="img/applications.png" class = "applimg" alt="Antagslogo"/><b>Wahl auf Studienkomission</b>
                </a></td>
            </tr>
        </table>

    </div>
</div>

<div class = "footer w3-animate-bottom">
    <table>
        <tr>
            <td><a href="https://www.w3schools.com/default.asp"><img src="img/footer/W3.png" alt = "W3 Logo"/><br>W3 schools</a></td>
            <td><a href="https://httpd.apache.org/"><img src="img/footer/apache.png" alt = "Apache Logo"/><br>Apache</a></td>
            <td><a href="https://www.stura.htw-dresden.de/"><img src="img/footer/Stura_htw.png" alt = "Stura Logo"/><br></a></td>
            <td><a href="https://www.gnu.org/home.de.html"><img src="img/footer/gnu.png" alt = "GNU Logo"/><br>GNU</a></td>
            <td><a href="https://www.bootstrapcdn.com/"><img src="img/footer/Bootstrap.png" alt = "Bootstrap Logo"/><br>BootstrapCDN</a></td>
        </tr>
    </table>
</div>
</body>
</html>
"""

print("Content-type: text/html\n\n")
print(html)
