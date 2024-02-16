<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loops</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>

<body>
    <div class="container">
        <form action="" class="form-control w-50 mx-auto" method="post">
            <div class="row">
                <div class="col-sm-12">
                    <b style="text-align:center;">
                        <h2>Loops</h2>
                    </b>
                </div>
                <hr>
                <br>
            </div>

            <div class="row">
                <div class="col-sm-12">
                    <p>
                        <input type="number" class="form-control" placeholder="N1" name="n1" id="n1">
                    </p>
                    <p>
                        <button class="btn btn-warning"name="f">For</button>
                        <button class="btn btn-success"name="w">While</button>
                        <button class="btn btn-info "name="d">Do</button>
                    </p>
                    <p>

                        <a href="atv1.php" class="btn btn-danger">Limpar</a>
                    </p>
                </div>
                <hr>
            </div>

            <div class="row p-5">
                <form action="" class="form-control">
                    <h4>
                    <?php
                    if ($_POST) {

                        $f = $_POST["n1"];
                        $i = 0;
 
                        if (isset($_POST["w"])) {

                            while ($i <= $f) {

                                echo $i++;
                                echo " - ";
                            }
                        }
                        elseif (isset($_POST["f"])) {
                            for ($i=0; $i <= $f ; $i++) { 
                                echo $i;
                                echo " - ";
                            }
                        
                        }
                        elseif (isset($_POST["d"])) {
                            do {
                                echo $i++;
                                echo " - ";
                            } while ($i <= $f);

                        }
                    }

                    ?>

                    </h4>
                </form>
            </div>
        </form>
    </div>

    <script src="js/bootstrap.js"></script>
</body>

</html>