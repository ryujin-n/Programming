<!DOCTYPE html>
<html lang="br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabela</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <script src="js/bootstrap.js"></script>
</head>

<body>
    <div class="container">
        <form action="" class="form-control" method="post">
            <div class="row">
                <div class="col-sm-12">
                    <b style="text-align:center;">
                        <h2>Tabela</h2>
                    </b>
                    <hr>
                </div>
            </div>

            <div class="row p-5">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>Nome</th>
                            <th>Bimestre 01</th>
                            <th>Bimestre 02</th>
                            <th>Bimestre 03</th>
                            <th>Bimestre 04</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php include_once("test.php");?>
                    </tbody>

                    <tfoot>
                        <tr>
                            <th>Total</th>
                        </tr>
                    </tfoot>
                </table>

                <p>
                    <input type="number" name="rw" id="rw" class="form-control w-25 " placeholder="Nº de Linhas"
                        required>
                </p>

                <p>
                    <button class="btn btn-success" name="w">OK</button>
                    <a href="atv2.php" class="btn btn-danger">Limpar</a>
                </p>

            </div>
        </form>
    </div>
</body>

</html>