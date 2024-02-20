<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/bootstrap.css">
    <title>Document</title>
</head>
<body>
    <div style="margin-top: 5rem;" class="container">
        <form action="" method="post" class="form-control">
            <div class="row">
                <div class="col-sm-12">
                    <h2>Formulário Simples</h2>
                    <br>
                </div>
                <div class="col-sm-6">
                    <p>
                        <label for="txtNome">Informe seu Nome</label>
                    </p>
                    <p>
                        <input type="text" id="txtNome" name="txtNome" class="form-control" required autocomplete="off">
                    </p>
                </div>
                <div class="col-sm-6">
                    <p>
                        <label for="txtSobrenome">Informe seu Sobrenome</label>
                    </p>
                    <p>
                        <input type="text" id="txtSobrenome" name="txtSobrenome" class="form-control" required autocomplete="off">
                    </p>
                </div>
                <div class="col-sm-4">
                    <p>
                        <button class="btn btn-success" formaction="pg02.php">Enviar</button>
                    </p>
                </div>
            </div>
        </form>
        <?php

            if($_POST){

                $namee = $_POST["txtNome"];
                $surnamee = $_POST["txtSobrenome"];


                echo "Seu nome completo é: " .$namee. " ". $surnamee;

            }

        ?>
    </div>

</body>
</html>