<?php

$id="";
$nome="";
$nasc="";
$data="";
$cnpj="";
$logr="";
$num="";
$comp="";
$cep="";
$bai="";
$cid="";
$uf="";
$tel="";
$cont="";
$obs="";
$sts="";

if ($_POST) {
    include_once("conn.php");

     //cadastro

     if (isset($_POST["cad"])) {
        try {
    
            $sql = $conn -> prepare('
                insert into fornecedor
                    (nome_Fornecedor,nasc_Fornecedor,cnpj_Fornecedor,logradouro_Fornecedor,numero_Fornecedor,cep_Fornecedor,bairro_Fornecedor,cidade_Fornecedor,uf_Fornecedor,telefone1_Fornecedor,contato_Fornecedor,obs_Fornecedor)
                values
                    (:nome_Fornecedor,
                    :nasc_Fornecedor,
                    :cnpj_Fornecedor,
                    :logradouro_Fornecedor,
                    :numero_Fornecedor,
                    :cep_Fornecedor,
                    :bairro_Fornecedor,
                    :cidade_Fornecedor,
                    :uf_Fornecedor,
                    :telefone1_Fornecedor,
                    :contato_Fornecedor,
                    :obs_Fornecedor)
            ');
        
            $sql -> execute(array(
                ':nome_Fornecedor' => $_POST['nome'],
                ':nasc_Fornecedor' =>$_POST['nasc'],
                ':cnpj_Fornecedor' =>$_POST['cnpj'],
                ':logradouro_Fornecedor' =>$_POST['logr'],
                ':numero_Fornecedor' =>$_POST['num'],
                ':cep_Fornecedor' => $_POST['cep'],
                ':bairro_Fornecedor' =>$_POST['bai'],
                ':cidade_Fornecedor' =>$_POST['cid'],
                ':uf_Fornecedor' =>$_POST['est'],
                ':telefone1_Fornecedor' =>$_POST['tel'],
                ':contato_Fornecedor' =>$_POST['obs'],
                ':obs_Fornecedor' =>$_POST['obs'],
            ));  
        
            if ($sql -> rowCount() > 0) {
                echo '<script>alert("Usuário Cadastrado com Sucesso")</script>';
                header("Location:atv3.php?IDUsuario=".$conn->lastInsertId());
            }
        } catch (PDOException $th) {
            echo $th;
        }
       
       } 
        //pesquisa
        elseif (isset($_POST['pesq'])) {
            try {
                $sql = $conn-> query('SELECT * FROM fornecedor where ID_Fornecedor='.$_POST['id'] );
                if ($sql->rowCount() > 0) {
                    foreach ($sql as $line) {

                        $id= $line[0];
                        $nome= $line[1];
                        $nasc= $line[2];
                        $data= $line[3];
                        $data = substr($data, 0, 10);
                        $cnpj= $line[4];
                        $logr= $line[5];
                        $num= $line[6];
                        $cep= $line[7];
                        $bai= $line[8];
                        $cid= $line[9];
                        $uf= $line[10];
                        $tel= $line[11];
                        $cont= $line[12];
                        $obs= $line[13];
                        $sts= $line[14];
                    }
                }
                else {
                     echo '<script>alert("Usuário não encontrado")</script>';
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

                $sql = $conn -> prepare('
                    UPDATE fornecedor SET

                        nome_Fornecedor = :nome_Fornecedor,
                        nasc_Fornecedor = :nasc_Fornecedor,
                        cnpj_Fornecedor = :cnpj_Fornecedor,
                        logradouro_Fornecedor = :logradouro_Fornecedor,
                        numero_Fornecedor = :numero_Fornecedor,
                        cep_Fornecedor = :cep_Fornecedor,
                        bairro_Fornecedor = :bairro_Fornecedor,
                        cidade_Fornecedor = :cidade_Fornecedor,
                        uf_Fornecedor = :uf_Fornecedor,
                        telefone1_Fornecedor = :telefone1_Fornecedor,
                        contato_Fornecedor = :contato_Fornecedor,
                        obs_Fornecedor = :obs_Fornecedor,
                        status_Fornecedor = :status_Fornecedor

                     WHERE ID_Fornecedor = :ID_Fornecedor
                    
                ');
            
                $sql -> execute(array(
                    ':ID_Fornecedor'=> $_POST['id'],
                    ':nome_Fornecedor' => $_POST['nome'],
                    ':nasc_Fornecedor' =>$_POST['nasc'],
                    ':cnpj_Fornecedor' =>$_POST['cnpj'],
                    ':logradouro_Fornecedor' =>$_POST['logr'],
                    ':numero_Fornecedor' =>$_POST['num'],
                    ':cep_Fornecedor' => $_POST['cep'],
                    ':bairro_Fornecedor' =>$_POST['bai'],
                    ':cidade_Fornecedor' =>$_POST['cid'],
                    ':uf_Fornecedor' =>$_POST['est'],
                    ':telefone1_Fornecedor' =>$_POST['tel'],
                    ':contato_Fornecedor' =>$_POST['tel'],
                    ':obs_Fornecedor' =>$_POST['obs'],
                    ':status_Fornecedor' => $_POST['sts']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Usuário Alterado com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
       }
       //deletar
       elseif (isset($_POST['del'])) {
        try {
            include_once('conn.php');
    
            $sql = $conn -> prepare('
                delete from fornecedor where ID_Fornecedor=:ID_Fornecedor
            ');
        
            $sql -> execute(array(
                ':ID_Fornecedor'=> $_POST['id']
            ));  
        
            if ($sql -> rowCount() > 0) {
                echo '<script>alert("Usuário Excluído com Sucesso")</script>';
            }
        } catch (PDOException $th) {
            echo $th;
        }
   }


}