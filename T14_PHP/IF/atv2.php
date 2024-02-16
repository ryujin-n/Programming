<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vendas</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>
<body>
    <div class="container">
         <form action="" method="post" class="form-control  w-50 mx-auto ">
            <div class="row">
                <div class="col-sm-12">
                    <b style="text-align:center;"><h2>Sistemas de Vendas</h2></b>
                    <hr>
                    <br>
                </div>
                <div class="col-sm 6">
                    <p>
                         <select name="prod" class="form-select" id="txtProd" required>
                            <option value=""> -- Produto-- </option>
                            <option value="a">A</option>
                            <option value="b">B</option>
                            <option value="c">C</option>
                            <option value="d">D</option>
                            <option value="e">E</option>
                            <option value="f">F</option>
                        </select>
                    </p>
                </div>
                <div class="col-sm 6">
                    <p>
                        <input type="number" name="txtQtde" id="txtQtde" class="form-control" placeholder="Quantidade" required min=0>
                    </p>
                </div>
            </div>

            <div class="row">
                <div class="col-sm 6">
                    <p>
                        <input type="number" name="txtVal" id="txtVal" class="form-control" placeholder="Valor Unitário" step="0.01" required>
                    </p>

                    <button class="btn btn-success mt-3 mb-3" id="btoOK" name="btoOK" formaction="atv2.php">Realizar Venda</button>
                    <a href="atv2.php" class="btn btn-danger">Apagar</a>

                    
                </div>
                <div class="col-sm 6">
                   
                    <p>
                        <select name="pgto" class="form-select" id="txtPgto" required>
                            <option value=""> -- Forma de Pagamento-- </option>
                            <option value="dn">Dinheiro</option>
                            <option value="px">Pix</option>
                            <option value="db">Débito</option>
                            <option value="cr">Crédito</option>
                            <option value="bl">Boleto</option>
                        </select>
                    </p>
                    
                </div>
                
            </div>
                <hr>
            <div class="row">
                <div class="col-sm-6 mx-auto">
                    <?php include_once("op2.php");?>
                    <p>
                        <br>
                        <label for="">Total:</label> 
                    </p>
                    <p>
                        <input type="text" name="txtTot" id="txtTot" class="form-control " value="<?php echo "R$". number_format($diff, 2) ?>" readonly>
                    </p>
                </div>
                <div class="col-sm-6 mx-auto">
                    <p>
                        <br>
                        <label for="">Total Real:</label> 
                    </p>
                    <p>

                        <input type="text" name="txtTotR" id="txtTotR" class="form-control" value="<?php echo "R$".number_format($total, 2) ?>" readonly>
                    </p>
                </div>
            </div>
            
            

        </form>
    </div>
    

    <script src="js/bootstrap.js"></script>
</body>
</html>
