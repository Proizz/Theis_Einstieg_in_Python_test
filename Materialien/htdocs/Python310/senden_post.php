<!DOCTYPE html><html>
<head>
   <meta charset="utf-8">
   <title>Daten empfangen</title>
</head>
<body>
   <b>Ihre folgenden Daten wurden registriert:</b><p>
   <?php
      $nn = htmlentities($_POST["nn"]);
      $vn = htmlentities($_POST["vn"]);
      echo "Nachname: $nn<br>Vorname: $vn";
   ?>
</body>
</html>
