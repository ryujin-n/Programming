    <!-- Desafio 01
 criar um sistema que leia 4 valores numéricos inteiro
 Imprimir a ordem crescente destes valores. -->


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/bootstrap.css">
    <title>Números Crescentes & Decrescentes</title>
</head>
<body>
    <div class="container">
         <form action="" method="post" class="form-control w-50 mx-auto">
            <div class="row">
                <div class="col-sm-12">
                <b style="text-align:center;"><h2>Números Crescentes & Decrescentes</h2></b>
                    <hr>
                    <br>
                </div>

                <div class="col-sm-6">
                   <p>
                        <input type="number" name="txtN1" class="form-control" id="txtN1" placeholder="Insira N1" required>
                   </p>
                </div>
                <div class="col-sm-6">
                   <p>
                        <input type="number" name="txtN2" class="form-control" id="txtN2" placeholder="Insira N2" required>
                   </p>                   
                </div>
            </div>

            <div class="row">
            <div class="col-sm-6">
                   <p>
                        <input type="number" name="txtN3" class="form-control" id="txtN3" placeholder="Insira N3" required>
                   </p>
                </div>
                <div class="col-sm-6">
                   <p>
                        <input type="number" name="txtN4" class="form-control" id="txtN4" placeholder="Insira N4" required>
                   </p>                   
                </div>

                <div class="col-sm-6">
                    <button class="btn btn-success mt-3 mb-3" id="btoOK" name="btoOK" formaction="ds1.php">OK</button>
                    <a href="ds1.php" class="btn btn-danger">Apagar</a>
                </div>
            </div>

            <hr>
            <br>

            <div class="row">
                <div class="col-sm-12">
                    <p>
                        <?php include_once('opd.php')?>
                        <label for=""> Resultado Crescente: </label> 
                        <input type="text" class="form-control " value="<?php echo $res; ?>" readonly>
                        <hr>
                        <label for=""> Resultado Decrescente: </label> 
                        <input type="text" class="form-control " value="<?php echo $resD; ?>" readonly>
                    </p>
                </div>
            </div>
        </form>
    </div>



    <script src="js/bootstrap.js"></script>
</body>
</html>