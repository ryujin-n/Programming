<!DOCTYPE html>
<html lang="br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalEstoque</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>

<body>

    <?php include_once("dados5.php");?>

    
    <div class="container">
        <form action="" method="post" class="form-control p-3">
             <div class="row">
                <div class="col-sm-12">
                    <hr>
                    <b style="text-align:center;"><h2>Armazém</h2></b>
                    <hr>
                    <br>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <p>
                        <input type="number" name="id" id="id" class="form-control" value="<?= $id;?>" placeholder="ID" >
                    </p>
                </div>
                <div class="col-sm-3">
                    <button class="btn btn-secondary " name="pesq" formaction="initial.php?tela=localest">
                        &#x1F50D;
                    </button>
                </div>
                <div class="col-sm-3"></div>
                <div class="col-sm-1"></div>
                <div class="col-sm-2">
                    <input type="date" name="data" id="data" class="form-control" value="<?= $data;?>">
                </div>
    
                <div class="row">
                    <div class="col-sm-6">
                        <p>
                            <input type="text" class="form-control" id="nome" name="nome" value="<?= $nome;?>" placeholder="Nome" >
                        </p>
                    </div>
                    <div class="col-sm-6">
                       
                        <p>
                            <select name="sts" id="sts" class="form-select w-50" placeholder="Status" >
                                <option value=""> -- Status -- </option>
                                <option value="ATIVO" <?=($sts=="ATIVO" )? "selected" : "" ?>>ATIVO</option>
                                <option value="INATIVO" <?=($sts=="INATIVO" )? "selected" : "" ?>>INATIVO</option>
                            </select>
                        </p>
                    </div>
                </div>
            
                </div>
                
                <div class="row">
                    <div class="col-sm-12">
                        <p>
                            <label for="obs">Observação</label>
                        </p>
                        <textarea name="obs" id="obs" rows="10" class="form-control"><?= $obs;?></textarea>
                        <br>
                    </div>
                </div>
    
                <div class="row">
                    <div class="col-sm-12 text-end">
                        <button class="btn btn-primary" name="cad" formaction=" initial.php?tela=localest">Cadastrar</button>
                        <button class="btn btn-success" name="alt"formaction=" initial.php?tela=localest">Alterar</button>
                        <a class="btn btn-dark" href=" initial.php?tela=localest">Limpar</a>
                        <button class="btn btn-danger" name="del" formaction=" initial.php?tela=localest">Excluir</button>
                        <hr>
                    </div>
                </div>
            </div>
        </form>


           
    </div>

    



    <script src="js/bootstrap.js"></script>
</body>

</html>
