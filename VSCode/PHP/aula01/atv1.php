<!DOCTYPE html>
<html lang="br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Média</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>
<body>
    <div style="margin: 5rem" class="container">
        <form action="" method="post" class="form-control  w-50  mx-auto">
            <div class="row">
                <div class="col-sm-12">
                    <h2  style="text-align: center;">Média Escolar</h2>
                    <br>
                    <h4>Insira suas notas aqui:</h4>
                    <br>
                </div>
                <div class="col-sm-6">
                    <p>
                        <label for="txtN1">Nota01</label>
                    </p>
                        <input type="number" name="txtN1" id="txtN1" class="form-control" required>
                    <p>

                    </p>
                </div>
                <div class="col-sm-6">
                    <p>
                        <label for="txtN2">Nota02</label>
                    </p>
                        <input type="number" name="txtN2" id="txtN2" class="form-control" required>
                    <p>

                    </p>
                </div>

            </div>

            <div class="row">
                <div class="col-sm-6">
                    <p>
                        <label for="txtN2">Nota03</label>
                    </p>
                        <input type="number" name="txtN3" id="txtN3" class="form-control" required>
                    <p>

                    </p>
                </div>
                <div class="col-sm-6">
                    <p>
                        <label for="txtN4">Nota04</label>
                    </p>
                        <input type="number" name="txtN4" id="txtN4" class="form-control" required>
                    <p>

                    </p>
                </div>

            </div>
            <button class="btn btn-primary" id="btoStat" name="btoStat" formaction="res.php">Enviar</button>
            
            <div class="row">
                <div class="col-sm-12">
                    <hr>
                    <br>
                    <h2>Status:</h2>
                    <br>

                    <input type="text" name="txtN4" id="txtN4" class="form-control" readonly>
                </div>
            </div>
        </form>
    </div>
</body>
</html>