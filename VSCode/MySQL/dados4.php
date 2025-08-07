<?php

$id="";
$nome="";
$data= "";
$vc="";
$vv="";
$qtde="";
$obs="";
$sts="";

    if ($_POST) {
        include_once("conn.php");

        //cadastro
        if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into produto
                        (nome_Produto,qtde_Produto,Vcusto_Produto,Vvenda_Produto,obs_Produto)
                    values
                        (:nome_Produto,:qtde_Produto,:Vcusto_Produto,:Vvenda_Produto,:obs_Produto)
                ');
            
                $sql -> execute(array(
                    ':nome_Produto' => $_POST['nome'],
                    ':qtde_Produto'=> $_POST['qtde'],
                    ':Vcusto_Produto'=> $_POST['vc'],
                    ':Vvenda_Produto'=> $_POST['vv'],
                    ':obs_Produto'=> $_POST['obs']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Produto Cadastrado com Sucesso")</script>';
                    header("Location:atv4.php?IDUsuario=".$conn->lastInsertId());
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           } 
        //pesquisa
        elseif (isset($_POST['pesq'])) {
            try {
                $sql = $conn-> query('SELECT * FROM produto where ID_Produto='.$_POST['id'] );
                if ($sql->rowCount() > 0) {
                    foreach ($sql as $line) {

                        $id=$line[0];
                        $nome=$line[1];
                        $data=$line[2];
                        $data=substr($data, 0, 10);
                        $qtde=$line[3];
                        $vc=$line[4];
                        $vv=$line[5];
                        $obs=$line[6];
                        $sts=$line[7];
                    }
                }
                else {
                     echo '<script>alert("Produto não encontrado")</script>';
                }
            }
             catch (PDOException $th)
            {
                echo $th;
            }
           }
        //alterar
        elseif (isset($_POST["alt"])) {
            try {
        
                $sql = $conn->prepare('
                    update produto set
                        nome_Produto = :nome_Produto,
                        qtde_Produto = :qtde_Produto,
                        Vcusto_Produto = :Vcusto_Produto,
                        Vvenda_Produto = :Vvenda_Produto,
                        obs_Produto = :obs_Produto,
                        status_Produto = :status_Produto
                    where ID_Produto = :ID_Produto
                ');
        
                $sql->execute(array(
                    ':ID_Produto' => $_POST['id'],
                    ':nome_Produto' => $_POST['nome'],
                    ':qtde_Produto' => $_POST['qtde'],
                    ':Vcusto_Produto' => $_POST['vc'],
                    ':Vvenda_Produto' => $_POST['vv'],
                    ':obs_Produto' => $_POST['obs'],
                    ':status_Produto' => $_POST['sts']
                ));
        
                if ($sql->rowCount() > 0) {
                    echo '<script>alert("Produto Alterado com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
        }
       elseif (isset($_POST['del'])) {
        try {
            include_once('conn.php');
    
            $sql = $conn -> prepare('
                delete from produto where ID_Produto=:ID_Produto
            ');
        
            $sql -> execute(array(
                ':ID_Produto'=> $_POST['id']
            ));  
        
            if ($sql -> rowCount() > 0) {
                echo '<script>alert("Produto Excluído com Sucesso")</script>';
            }
        } catch (PDOException $th) {
            echo $th;
        }
   }
    }