<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
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
                        <label for="txtProd">Produto</label>
                    </p>
                    <p>
                        <input type="text" name="txtProd" id="txtProd" class="form-control" required>
                    </p>
                </div>
                <div class="col-sm 6">
                    <p>
                        <label for="txtQtde">Quantidade</label>
                    </p>
                    <p>
                        <input type="number" name="txtQtde" id="txtQtde" class="form-control" required min=0>
                    </p>
                </div>
            </div>

            <div class="row">
                <div class="col-sm 6">
                    <p>
                        <label for="txtVal">Valor Unitário</label>
                    </p>
                    <p>
                        <input type="text" name="txtVal" id="txtVal" class="form-control" required>
                    </p>

                    <button class="btn btn-success" id="btoOK" name="btoOK" formaction="op2.php">Realizar Venda</button>
                    
                </div>
                <div class="col-sm 6">
                    <p>
                        Forma de Pagamento
                    </p>
                    <p>
                        <select name="pgto" class="form-select" id="txtPgto" name="txtPgto">
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
            
            <div style=" margin-top: 1rem; background-color:lightslategray; height:100px; border-radius:10px; font-family: Arial, Helvetica, sans-serif; color: white; text-align: center;" class="p-3">
                    <p>
                        Valor: <?php  ?>
                    </p>

                    <p>
                        Valor Real: <?php  ?>
                    </p>
                </div>

            </div>

        </form>
    </div>
    

    <script src="js/bootstrap.js"></script>
</body>
</html>
