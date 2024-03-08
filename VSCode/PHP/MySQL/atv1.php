<!DOCTYPE html>
<html lang="br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/bootstrap.css">
    
    <title>Usuário</title>
</head>

<body>
    
    <?php
        include_once('dados.php');   
        ?>
    <div class="container">
        <form action="" method="post" onsubmit="return false;" class="form-control p-3" enctype="multipart/form-data" id="form">
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
                    <button class="btn btn-secondary " name="pesq" onclick="enviar('pes')">
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
                        <input type="file" name="img" id="img" class="form-control">
                        <span name="img2" id="img2"style="display:none;"><?= $img; ?></span>
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-4">
                    <p>
                        <input type="text" name="user" id="userr" class="form-control" placeholder="Usuário" value="<?=$Login?>">
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
                        <img src="src/<?= $idUsuario ?>/<?= $img ?>" alt="" id="pic" class="w-100" >
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12 text-end">
                    <button class="btn btn-primary" name="cad" onclick="enviar('cad')" >Cadastrar</button>
                    <button class="btn btn-success" name="alt" onclick="enviar('alter')">Alterar</button>
                    <button class="btn btn-dark"onclick="limpar()">Limpar</button>
                    <button class="btn btn-danger" name="del" onclick="enviar('del')">Excluir</button>
                    <input type="text" name="action" id="action" style="">
                    <hr>
                </div>
            </div>
        </div>
    </form>
    
    <script src="js/bootstrap.js"></script>

    <script>

        const form = document.getElementById("form")
        const id =document.getElementById("id")
        const date = document.getElementById("data")
        const user = document.getElementById("userr")
        const pass = document.getElementById("senha")
        const name = document.getElementById("nome")
        const sts = document.getElementById("sts")
        const img = document.getElementById("img")
        const obs = document.getElementById("obs")
        const action = document.getElementById("action")
        const pic = document.getElementById("pic")
        const caminho = "initial.php?tela=usuario"


        function enviar(type)
        {
            if (type == 'pes') {

                if (id.value==""){
                    alert("O ID deve ser Preenchido")
                    id.focus()
                    return;
                }
                action.value = 'pesq'
                form.action = caminho
                form.submit()
            }
            else if(type == 'cad'){
                
                if (name.value==""){
                    alert("O Nome deve ser Preenchido")
                    name.focus()
                    return;
                }
                else if (user.value == ""){
                    alert("O Usuário deve ser Preenchido")
                    user.focus()
                    return;
                }
                else if (pass.value == ""){
                    alert("A Senha deve ser Preenchido")
                    pass.focus()
                    return;
                }
                else if (img.value == ""){
                    alert("A imagem deve ser Preenchido")
                    img.focus()
                    return;
                }
                else if (sts.value == ""){
                    alert("O Status deve ser Preenchido")
                    sts.focus()
                    return;
                }
                action.value='cadas'
                form.action = caminho
                form.submit()
            }
            else if(type == 'alter'){
                if (name.value==""){
                    alert("O Nome deve ser Preenchido")
                    name.focus()
                    return;
                }
                else if (user.value == ""){
                    alert("O Usuário deve ser Preenchido")
                    user.focus()
                    return;
                }
                else if (pass.value == ""){
                    alert("A Senha deve ser Preenchido")
                    pass.focus()
                    return;
                }
               
                else if (sts.value == ""){
                    alert("O Status deve ser Preenchido")
                    sts.focus()
                    return;
                }

                action.value='alter'
                form.action = caminho
                form.submit()
            }
            else if(type == 'del'){
                
                action.value='del'

                if(id.value=="")
                {
                    alert ("Valor do ID deve ser preenchido")
                    id.focus()
                    return;
                }
                //alert(type)

                form.action=caminho
                form.submit()

            }
        }
        function limpar() {
            id.value = ""
            date.value = ""
            user.value = ""
            pass.value = ""
            name.value = ""
            sts.value = ""
            img.value = ""
            obs.value = ""
            pic.src = "" 
        }

    </script>

    <script>
            const urlParams = new URLSearchParams(window.location.search);
            const userId = urlParams.get('IDUsuario');
            
            if (userId) {
                alert("Usuário cadastrado com sucesso");
            }
    </script>
</body>

</html>