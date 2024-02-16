<!-- Desafio 02
 Criar um sistema que faça a validação de dados de uma tela de cadastro de clientes
ID, nome, data nascimento, rua, numero, complemento, cep, bairro, cidade, estado, pais, observação, status

Não apagar os dados caso o valor não seja preenchido -->



<!DOCTYPE html>
<html lang="br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>

<body>


    <style>
        .error-message {
            position: fixed;
            bottom: 20px; 
            right: 20px; 
            z-index: 9999; 
        }
    </style>


    <?php include_once("opd2.php");?>

    
    <div class="container">
        <?php if (!empty($error_message)): ?>
                    <div class="alert alert-danger error-message" role="alert">
                        <?php echo $error_message; ?>
                    </div>
                <?php endif; ?>
        <form action="" method="post" class="form-control">
             <div class="row">
                <div class="col-sm-12">
                    <b style="text-align:center;"><h2>Sistema de Cadastro</h2></b>
                    <hr>
                    <br>
                </div>

                <div class="col-sm-2">
                    <p>
                        <label for="id">ID</label>
                    </p>
                    <p>
                        <input type="number" name="id" id="id" class="form-control w-50" value="<?= $id;?>">
                    </p>
                </div>

                <div class="col-sm-2">
                     <p>
                        <label for="sts">Status</label>
                    </p>
                    <p>
                        <select name="sts" id="sts" class="form-control">
                            <option value=" -- Status -- "></option>
                            <option value="on" <?= ($status == "on")? "selected" : "" ?>>Ativo</option>
                            <option value="off"<?= ($status == "off")? "selected" : "" ?>>Inativo</option>
                        </select>
                    </p>
                    <br>
                </div>

                <div class="row">
                    <div class="col-sm-4">
                        
                        <p>
                            <label for="nome"> Nome Completo</label>
                        </p>
                    
                        <p>
                            <input type="text" class="form-control" id="nome" name="nome" value="<?= $name;?>">
                        </p>
                    </div>
                    <div class="col-sm-4">
                         <p>
                            <label for="data"> Data de Nascimento</label>
                        </p>

                        <p>
                            <input type="date" class="form-control" name="data" value="<?= $data;?>">
                        </p>
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-3">
                        
                        <p>
                            <label for="cep"> Cep </label>
                        </p>
                    
                        <p>
                            <input type="text" class="form-control" id="cep" name="cep" value="<?= $postal;?>">
                        </p>
                    </div>
                    <div class="col-sm-3">
                         <p>
                            <label for="rua"> Rua </label>
                        </p>

                        <p>
                            <input type="text" class="form-control" name="rua" value="<?= $street;?>" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                         <p>
                            <label for="comp"> Complemento </label>
                        </p>
                    
                        <p>
                            <input type="text" class="form-control" id="comp" name="comp" value="<?= $comp;?>">
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>

                             <label for="nome"> Número</label>
                        </p>

                        <p>
                            <input type="number" class="form-control w-25" name="num" value="<?= $number;?>" >
                        </p>
                       
                    </div>
                </div>

                <div class="row">
                   
                    <div class="col-sm-3">
                         <p>
                            <label for="bai"> Bairro </label>
                        </p>

                        <p>
                            <input type="text" class="form-control" name="bai" value="<?= $nbd;?>" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                         <p>
                            <label for="nome"> Cidade </label>
                        </p>

                        <p>
                            <input type="text" class="form-control" name="cid" value="<?= $city;?>" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                            <p>
                                <label for="est"> Estado </label>
                        </p>
    
                        <p>
                        <select name="est" class="form-control">
                            <option value=""> -- Escolha um Estado --</option>
                            <option value="ac" <?= ($state == "ac")? "selected" : "" ?>>Acre</option>
                            <option value="al" <?= ($state == "al")? "selected" : "" ?>>Alagoas</option>
                            <option value="ap" <?= ($state == "ap")? "selected" : "" ?>>Amapá</option>
                            <option value="am" <?= ($state == "am")? "selected" : "" ?>>Amazonas</option>
                            <option value="ba" <?= ($state == "ba")? "selected" : "" ?>>Bahia</option>
                            <option value="ce" <?= ($state == "ce")? "selected" : "" ?>>Ceará</option>
                            <option value="df" <?= ($state == "df")? "selected" : "" ?>>Distrito Federal</option>
                            <option value="es" <?= ($state == "es")? "selected" : "" ?>>Espírito Santo</option>
                            <option value="go" <?= ($state == "go")? "selected" : "" ?>>Goiás</option>
                            <option value="ma" <?= ($state == "ma")? "selected" : "" ?>>Maranhão</option>
                            <option value="mt" <?= ($state == "mt")? "selected" : "" ?>>Mato Grosso</option>
                            <option value="ms" <?= ($state == "ms")? "selected" : "" ?>>Mato Grosso do Sul</option>
                            <option value="mg" <?= ($state == "mg")? "selected" : "" ?>>Minas Gerais</option>
                            <option value="pa" <?= ($state == "pa")? "selected" : "" ?>>Pará</option>
                            <option value="pb" <?= ($state == "pb")? "selected" : "" ?>>Paraíba</option>
                            <option value="pr" <?= ($state == "pr")? "selected" : "" ?>>Paraná</option>
                            <option value="pe" <?= ($state == "pe")? "selected" : "" ?>>Pernambuco</option>
                            <option value="pi" <?= ($state == "pi")? "selected" : "" ?>>Piauí</option>
                            <option value="rj" <?= ($state == "rj")? "selected" : "" ?>>Rio de Janeiro</option>
                            <option value="rn" <?= ($state == "rn")? "selected" : "" ?>>Rio Grande do Norte</option>
                            <option value="rs" <?= ($state == "rs")? "selected" : "" ?>>Rio Grande do Sul</option>
                            <option value="ro" <?= ($state == "ro")? "selected" : "" ?>>Rondônia</option>
                            <option value="rr" <?= ($state == "rr")? "selected" : "" ?>>Roraima</option>
                            <option value="sc" <?= ($state == "sc")? "selected" : "" ?>>Santa Catarina</option>
                            <option value="sp" <?= ($state == "sp")? "selected" : "" ?>>São Paulo</option>
                            <option value="se" <?= ($state == "se")? "selected" : "" ?>>Sergipe</option>
                            <option value="to" <?= ($state == "to")? "selected" : "" ?>>Tocantins</option>
                        </select>
                        </p>
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
                    <div class="col-sm-12">
                        <button class="btn btn-success">OK</button>
                        <a href="ds2.php" class="btn btn-danger">Limpar</a>
                    </div>
                </div>
            </div>
        </form>
           
    </div>

    



    <script src="js/bootstrap.js"></script>
</body>

</html>
