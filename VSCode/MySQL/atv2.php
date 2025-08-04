<!DOCTYPE html>
<html lang="br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funcionário</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>

<body>

    <?php include_once("dados2.php");?>

    
    <div class="container">
     <form action="" method="post" onsubmit="return false;" class="form-control p-3" enctype="multipart/form-data" id="form">
             <div class="row">
                <div class="col-sm-12">
                    <hr>
                    <b style="text-align:center;"><h2>Funcionário</h2></b>
                    <hr>
                    <br>
                </div>

                <div class="col-sm-3">
                    <p>
                        <input type="number" name="id" id="id" class="form-control" value="<?= $id;?>" placeholder="ID" >
                    </p>
                </div>
                <div class="col-sm-3">
                    <button class="btn btn-secondary " name="pesq" onclick="enviar('pes')">
                        &#x1F50D;
                    </button>
                </div>
                <div class="col-sm-3"></div>
                <div class="col-sm-1"></div>
                <div class="col-sm-2">
                    <input type="date" name="data" id="data" class="form-control" value="<?= $data;?>">
                </div>

                <div class="row">
                    <div class="col-sm-8">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="text" class="form-control" id="nome" name="nome" value="<?= $nome;?>" placeholder="Nome Completo" >
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
                    <div class="col-sm-3">
                         <p>
                            <label for="data"> Data de Nascimento</label>
                        </p>

                        <p>
                            <input type="date" class="form-control" name="nasc" id="nasc" value="<?= $nasc;?>" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="text" class="form-control " name="cpf" id="cpf" value="<?= $cpf;?>"placeholder="CPF"  >
                        </p>
                       
                    </div>
                    <div class="col-sm-3">
                        <p>
                            &nbsp;
                        </p>
                        <p>
                            <input type="tel" class="form-control " name="tel" id="tel" value="<?= $tel;?>"placeholder="Telefone"  >
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
                            <input type="text" class="form-control" name="logr" id="logr" value="<?= $logr;?>" placeholder="Rua" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            <input type="text" class="form-control" id="comp" name="comp" value="<?= $comp;?>"placeholder="Complemento" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            <input type="number" class="form-control w-25" name="num" id="num" value="<?= $num;?>"placeholder="Nº"  >
                        </p>
                       
                    </div>
                   
                </div>

                <div class="row">
                   
                    <div class="col-sm-3">
                        <p>
                            <input type="text" class="form-control" name="bai" id="bai" value="<?= $bai;?>" placeholder="Bairro" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                            <input type="text" class="form-control" name="cid" id="cid" value="<?= $cid;?>" placeholder="Cidade" >
                        </p>
                    </div>
                    <div class="col-sm-3">
                        <p>
                        <select name="est" class="form-control" id="est" >
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
                    <div class="col-sm-7">
                        <p>
                            <label for="obs">Observação</label>
                        </p>
                        <textarea name="obs" id="obs" rows="10" class="form-control"><?= $obs;?></textarea>
                        <br>
                    </div>
                    <div class="col-sm-5">
                        <img src="src2/<?=$idUsuario?>/<?=$img?>" id="pic" alt="" class="w-100">
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-12 text-end">
                        <button class="btn btn-primary" name="cad" onclick="enviar('cad')" >Cadastrar</button>
                        <button class="btn btn-success" name="alt" onclick="enviar('alter')">Alterar</button>
                        <button class="btn btn-dark"onclick="limpar()">Limpar</button>
                        <button class="btn btn-danger" name="del" onclick="enviar('del')">Excluir</button>
                        <input type="text" name="action" id="action" style="">
                        <p><?=$msg?></p>
                        <hr>
                    </div>
                </div>
            </div>
        </form>
           
    </div>

    



    <script src="js/bootstrap.js"></script>

    <script>

        const form = document.getElementById("form")
        const id =document.getElementById("id")
        const date = document.getElementById("data")
        const name = document.getElementById("nome")
        const nasc = document.getElementById("nasc")
        const cpf = document.getElementById("cpf")
        const tel = document.getElementById("tel")
        const sts = document.getElementById("sts")
        const cep = document.getElementById("cep")
        const logr = document.getElementById("logr")
        const comp = document.getElementById("comp")
        const num = document.getElementById("num")
        const bai = document.getElementById("bai")
        const cid = document.getElementById("cid")
        const est = document.getElementById("est")
        const obs = document.getElementById("obs")
        const img = document.getElementById("img")
        const action = document.getElementById("action")
        const pic = document.getElementById("pic")
        const caminho = "initial.php?tela=func"


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
                else if (nasc.value == ""){
                    alert("A Data de Nascimento deve ser Preenchida")
                    nasc.focus()
                    return;
                }
                else if (cpf.value == ""){
                    alert("O CPF deve ser Preenchido")
                    cpf.focus()
                    return;
                }
                else if (tel.value == ""){
                    alert("O Telefone deve ser Preenchido")
                    tel.focus()
                    return;
                }
                else if (sts.value == ""){
                    alert("O Status deve ser Preenchido")
                    sts.focus()
                    return;
                }
                else if (cep.value == ""){
                    alert("O Cep deve ser Preenchido")
                    cep.focus()
                    return;
                }
                else if (logr.value == ""){
                    alert("O Logradouro deve ser Preenchido")
                    logr.focus()
                    return;
                }
                else if (comp.value == ""){
                    alert("O Complemento deve ser Preenchido")
                    comp.focus()
                    return;
                }
                else if (num.value == ""){
                    alert("O Número deve ser Preenchido")
                    num.focus()
                    return;
                }
                else if (bai.value == ""){
                    alert("O Bairro deve ser Preenchido")
                    bai.focus()
                    return;
                }
                else if (cid.value == ""){
                    alert("A Cidade deve ser Preenchida")
                    cid.focus()
                    return;
                }
                else if (est.value == ""){
                    alert("O UF deve ser Preenchido")
                    est.focus()
                    return;
                }
                
                else if (obs.value == ""){
                    alert("A Observação deve ser Preenchida")
                    obs.focus()
                    return;
                }
                
                else if (img.value == ""){
                    alert("A imagem deve ser Preenchida")
                    img.focus()
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
                else if (nasc.value == ""){
                    alert("A Data de Nascimento deve ser Preenchida")
                    nasc.focus()
                    return;
                }
                else if (cpf.value == ""){
                    alert("O CPF deve ser Preenchido")
                    cpf.focus()
                    return;
                }
                else if (tel.value == ""){
                    alert("O Telefone deve ser Preenchido")
                    tel.focus()
                    return;
                }
                else if (sts.value == ""){
                    alert("O Status deve ser Preenchido")
                    sts.focus()
                    return;
                }
                else if (cep.value == ""){
                    alert("O Cep deve ser Preenchido")
                    cep.focus()
                    return;
                }
                else if (logr.value == ""){
                    alert("O Logradouro deve ser Preenchido")
                    logr.focus()
                    return;
                }
                else if (comp.value == ""){
                    alert("O Complemento deve ser Preenchido")
                    comp.focus()
                    return;
                }
                else if (num.value == ""){
                    alert("O Número deve ser Preenchido")
                    num.focus()
                    return;
                }
                else if (bai.value == ""){
                    alert("O Bairro deve ser Preenchido")
                    bai.focus()
                    return;
                }
                else if (cid.value == ""){
                    alert("A Cidade deve ser Preenchida")
                    cid.focus()
                    return;
                }
                else if (est.value == ""){
                    alert("O UF deve ser Preenchido")
                    est.focus()
                    return;
                }
                
                else if (obs.value == ""){
                    alert("A Observação deve ser Preenchida")
                    obs.focus()
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

                form.action=caminho
                form.submit()

            }
        }
        function limpar() {
            id.value = ""
            date.value = ""
            name.value = ""
            nasc.value = ""
            cpf.value = ""
            tel.value = ""
            sts.value = ""
            cep.value = ""
            logr.value = ""
            comp.value = ""
            num.value = ""
            bai.value = ""
            cid.value = ""
            est.value = ""
            obs.value = ""
            img.value = ""
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
