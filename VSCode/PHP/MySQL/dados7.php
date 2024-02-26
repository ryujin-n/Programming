<?php

    $id="";
    $idp="";
    $idf="";
    $qtde="";
    $data="";
    $tpo="";
    $obs="";
    $sts="";

    if ($_POST) {
        include_once("conn.php");

          //cadastro
          if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into movimentacao
                        (id_Produto_mov,id_funcionario_mov,qtde_os,tipo_mov,obs_mov)
                    values
                        (:id_produto_os,:qtde_os,:obs_os)
                ');
            
                $sql -> execute(array(
                    ':id_produto_os' => $_POST['idp'],
                    ':qtde_os' => $_POST['qtde'],
                    ':obs_os'=> $_POST['obs']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Ordem Cadastrada com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           }
    }