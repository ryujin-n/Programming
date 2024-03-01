<!DOCTYPE html>
<html lang="br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/bootstrap.css">
    <script src="js/bootstrap.js"></script>

    <title>Usuário</title>
</head>

<body>

    <?php
        include_once('dados.php')    
    ?>
    <div class="container">
        <form action="" method="post" class="form-control p-3" enctype="multipart/form-data">
            <div class="row">
                <div class="col-sm-12">
                    <b style="text-align:center;">
                        <hr>
                        <h2>Usuário</h2>
                        <hr>
                        <br>
                    </b>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <p>
                        <input type="number" name="id" id="id" class="form-control" placeholder="ID" value="<?=$ID?>">
                    </p>
                </div>
                <div class="col-sm-3">
                    <button class="btn btn-secondary " name="pesq" formaction="initial.php?tela=usuario">
                        &#x1F50D;
                    </button>
                </div>
                <div class="col-sm-3"></div>
                <div class="col-sm-3">
                    <input type="date" name="data" id="data" class="form-control" value="<?=$Data?>">
                </div>
            </div>

            <div class="row">
            <div class="col-sm-8">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="text" class="form-control" id="nome" name="nome" value="<?= $Nome;?>" placeholder="Nome Completo" >
                        </p>
                    </div>
                    <div class="col-sm-4">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="file" name="img" id="img" class="form-control" value="<?=$img?>">
                        </p>
                    </div>
            </div>
            <div class="row">
                <div class="col-sm-4">
                    <p>
                        <input type="text" name="user" id="user" class="form-control" placeholder="Usuário" value="<?=$Login?>">
                    </p>
                </div>
                <div class="col-sm-4">
                    <p>
                        <input type="password" name="senha" id="senha" class="form-control" placeholder="Senha" value="<?=$Senha?>">
                    </p>
                </div>
                <div class="col-sm-4">
                    <select class="form-select w-50" name="sts" id="sts">
                        <option value=""> -- Status -- </option>
                        <option value="ATIVO"<?=($Status=='ATIVO')?'Selected':'';?>>ATIVO</option>
                        <option value="INATIVO"<?=($Status=='INATIVO')?'Selected':'';?>>INATIVO</option>
                    </select>
                    <br>
                    <br>
                </div>
            </div>
            <div class="row">
                <div class="row">
                        <div class="col-sm-7">
                            <p>
                                <label for="obs">Observação</label>
                            </p>
                            <textarea name="obs" id="obs" rows="10" class="form-control"><?= $Obs; ?></textarea>
                        <br>
                    </div>
                    <div class="col-sm-5">
                        <img src="src/<?= $idUsuario ?>/<?= $img ?>" alt="" class="w-100">
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12 text-end">
                    <button class="btn btn-primary" name="cad" formaction="initial.php?tela=usuario">Cadastrar</button>
                    <button class="btn btn-success" name="alt"formaction="initial.php?tela=usuario">Alterar</button>
                    <a class="btn btn-dark" href="initial.php?tela=usuario">Limpar</a>
                    <button class="btn btn-danger" name="del" formaction="initial.php?tela=usuario">Excluir</button>
                    <hr>
                </div>
            </div>
        </div>
    </form>
</body>

</html>