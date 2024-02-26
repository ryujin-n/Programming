<!DOCTYPE html>
<html lang="br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>

<body>

    <?php include_once("dados3.php");?>

    
    <div class="container">
        <form action="" method="post" class="form-control p-3">
             <div class="row">
                <div class="col-sm-12">
                    <hr>
                    <b style="text-align:center;"><h2>Fornecedor</h2></b>
                    <hr>
                    <br>
                </div>

                <div class="col-sm-3">
                    <p>
                        <input type="number" name="id" id="id" class="form-control" value="<?= $id;?>" placeholder="ID" >
                    </p>
                </div>
                <div class="col-sm-3">
                    <button class="btn btn-secondary " name="pesq" formaction="atv3.php">
                        &#x1F50D;
                    </button>
                </div>
                <div class="col-sm-3"></div>
                <div class="col-sm-1"></div>
                <div class="col-sm-2">
                    <input type="date" name="data" id="data" class="form-control" value="<?= $data;?>">
                </div>

                <div class="row">
                    <div class="col-sm-12">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="text" class="form-control" id="nome" name="nome" value="<?= $nome;?>" placeholder="Nome" >
                        </p>
                    </div>
                </div>
                
                <div class="row">
                    <div class="col-sm-3">
                         <p>
                            <label for="data"> Data de Nascimento</label>
                        </p>

                        <p>
                            <input type="date" class="form-control" name="nasc" value="<?= $nasc;?>" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="text" class="form-control " name="cnpj" value="<?= $cnpj;?>"placeholder="CNPJ"  >
                        </p>
                       
                    </div>
                    <div class="col-sm-3">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="text" class="form-control " name="tel" value="<?= $tel;?>"placeholder="Telefone"  >
                        </p>
                       
                    </div>
                    <div class="col-sm-3">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <select name="sts" id="sts" class="form-select w-50" placeholder="Status" >
                                <option value=""> -- Status -- </option>
                                <option value="ATIVO" <?=($sts=="ATIVO" )? "selected" : "" ?>>ATIVO</option>
                                <option value="INATIVO" <?=($sts=="INATIVO" )? "selected" : "" ?>>INATIVO</option>
                            </select>
                        </p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-3">
                        <p>
                            <input type="text" class="form-control" id="cep" name="cep" value="<?= $cep;?>"placeholder="Cep" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            <input type="text" class="form-control" name="logr" value="<?= $logr;?>" placeholder="Rua" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            <input type="number" class="form-control w-25" name="num" value="<?= $num;?>"placeholder="Nº"  >
                        </p>
                       
                    </div>
                   
                </div>

                <div class="row">
                   
                    <div class="col-sm-3">
                        <p>
                            <input type="text" class="form-control" name="bai" value="<?= $bai;?>" placeholder="Bairro" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            <input type="text" class="form-control" name="cid" value="<?= $cid;?>" placeholder="Cidade" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                        <select name="est" class="form-control" >
                            <option value=""> -- Escolha um Estado --</option>
                            <option value="ac" <?= ($uf == "ac")? "selected" : "" ?>>Acre</option>
                            <option value="al" <?= ($uf == "al")? "selected" : "" ?>>Alagoas</option>
                            <option value="ap" <?= ($uf == "ap")? "selected" : "" ?>>Amapá</option>
                            <option value="am" <?= ($uf == "am")? "selected" : "" ?>>Amazonas</option>
                            <option value="ba" <?= ($uf == "ba")? "selected" : "" ?>>Bahia</option>
                            <option value="ce" <?= ($uf == "ce")? "selected" : "" ?>>Ceará</option>
                            <option value="df" <?= ($uf == "df")? "selected" : "" ?>>Distrito Federal</option>
                            <option value="es" <?= ($uf == "es")? "selected" : "" ?>>Espírito Santo</option>
                            <option value="go" <?= ($uf == "go")? "selected" : "" ?>>Goiás</option>
                            <option value="ma" <?= ($uf == "ma")? "selected" : "" ?>>Maranhão</option>
                            <option value="mt" <?= ($uf == "mt")? "selected" : "" ?>>Mato Grosso</option>
                            <option value="ms" <?= ($uf == "ms")? "selected" : "" ?>>Mato Grosso do Sul</option>
                            <option value="mg" <?= ($uf == "mg")? "selected" : "" ?>>Minas Gerais</option>
                            <option value="pa" <?= ($uf == "pa")? "selected" : "" ?>>Pará</option>
                            <option value="pb" <?= ($uf == "pb")? "selected" : "" ?>>Paraíba</option>
                            <option value="pr" <?= ($uf == "pr")? "selected" : "" ?>>Paraná</option>
                            <option value="pe" <?= ($uf == "pe")? "selected" : "" ?>>Pernambuco</option>
                            <option value="pi" <?= ($uf == "pi")? "selected" : "" ?>>Piauí</option>
                            <option value="rj" <?= ($uf == "rj")? "selected" : "" ?>>Rio de Janeiro</option>
                            <option value="rn" <?= ($uf == "rn")? "selected" : "" ?>>Rio Grande do Norte</option>
                            <option value="rs" <?= ($uf == "rs")? "selected" : "" ?>>Rio Grande do Sul</option>
                            <option value="ro" <?= ($uf == "ro")? "selected" : "" ?>>Rondônia</option>
                            <option value="rr" <?= ($uf == "rr")? "selected" : "" ?>>Roraima</option>
                            <option value="sc" <?= ($uf == "sc")? "selected" : "" ?>>Santa Catarina</option>
                            <option value="sp" <?= ($uf == "sp")? "selected" : "" ?>>São Paulo</option>
                            <option value="se" <?= ($uf == "se")? "selected" : "" ?>>Sergipe</option>
                            <option value="to" <?= ($uf == "to")? "selected" : "" ?>>Tocantins</option>
                        </select>
                        </p>
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-3">
                        <input type="text" class="form-control" name="cont" value="<?= $cont;?>" placeholder="Contato" >
                        <br>
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
                        <button class="btn btn-primary" name="cad" formaction="atv3.php">Cadastrar</button>
                        <button class="btn btn-success" name="alt"formaction="atv3.php">Alterar</button>
                        <a class="btn btn-dark" href="atv3.php">Limpar</a>
                        <button class="btn btn-danger" name="del" formaction="atv3.php">Excluir</button>
                        <hr>
                    </div>
                </div>
            </div>
        </form>
           
    </div>

    



    <script src="js/bootstrap.js"></script>
</body>

</html>
