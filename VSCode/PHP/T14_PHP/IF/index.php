<!DOCTYPE html>
<html lang="br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Meu Primeiro PHP :)</h1>
    <hr>

    <?php 

        $name = "Miles";
        $surname = "Jesus";
        $age = "20";

        date_default_timezone_set('America/Sao_Paulo');

        echo "<h2>hello world!</h2>";
        echo "<p>hello world!</p>";
        echo "<hr>";
        echo date ("d/m/Y");
        echo "<br>";
        echo date("H:i:s");

        echo "<br>";
        echo "<hr>";
        echo "Seu nome completo é: " . "<b>$name</b>" . " <b>$surname</b>" . " e sua idade é: " . "<i>$age </i>" . "anos"

    ?>

    <script src="js/bootstrap.js"></script>
</body>
</html>