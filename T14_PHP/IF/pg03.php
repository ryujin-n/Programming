<!DOCTYPE html>
<html lang="br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>
<body>
    <div style="margin-top: 5rem;" class="container">
        <form action="" method="post" class="form-control">            
            <div class="row">
                <div class="col-sm-12">
                    <h2>Calculadora</h2>
                    <br>
                </div>
                <div class="col-sm-6">
                  <p>
                    <label for="txtN1">N1</label>
                  </p>

                  <p>
                      <input type="number" name="txtN1" class="form-control" id="txtN1" placeholder="Numero1">
                  </p>
                </div>
                <div class="col-sm-6">
                  <p>
                    <label for="txtN2">N1</label>
                  </p>

                  <p>
                      <input type="number" name="txtN2" class="form-control" id="txtN2" placeholder="Numero2">
                  </p>
                </div>
            </div>

            <div class="col-sm-12">
                <button class="btn btn-success" id="btoMais" name="btoMais" formaction="pg03.php">+</button>
                <button class="btn btn-primary" id="btoMenos" name="btoMenos" formaction="pg03.php">-</button>
                <button class="btn btn-info" id="btoVezes" name="btoVezes" formaction="pg03.php">*</button>
                <button class="btn btn-warning" id="btoDividir" name="btoDividir" formaction="pg03.php">/</button>
            </div>
        </form>
        <hr>
        <?php 
            include_once('op.php');
        ?>
    </div>
</body>
</html>

