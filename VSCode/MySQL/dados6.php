<?php

$id="";
$idp="";
$data="";
$qtde="";
$obs="";
$sts="";

    if ($_POST) {
        include_once("conn.php");

         //cadastro
         if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into os
                        (id_produto_os,qtde_os,obs_os)
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
                    header("Location:atv6.php?IDUsuario=".$conn->lastInsertId());
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           }
           //pesquisa
           elseif (isset($_POST['pesq'])) {
            try {
                $sql = $conn-> query('SELECT * FROM os where id_os='.$_POST['id'] );
                if ($sql->rowCount() > 0) {
                    foreach ($sql as $line) {

                        $id=$line[0];
                        $idp=$line[1];
                        $data=$line[2];
                        $data= substr($data, 0, 10);
                        $qtde=$line[3];
                        $obs=$line[4];
                        $sts=$line[5];
                    }
                }
                else {
                     echo '<script>alert("Ordem não encontrada")</script>';
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
                    UPDATE os SET
                        id_produto_os = :id_produto_os,
                        qtde_os = :qtde_os,
                        obs_os = :obs_os,
                        status_os = :status_os
                    WHERE id_os = :id_os
                ');

            $sql->execute(
                array(
                    ':id_os' => $_POST['id'],
                    ':id_produto_os' => $_POST['idp'],
                    ':qtde_os' => $_POST['qtde'],
                    ':obs_os' => $_POST['obs'],
                    ':status_os' => $_POST['sts']
                )
            );

            if ($sql -> rowCount() > 0) {
                        echo '<script>alert("Ordem Alterada com Sucesso")</script>';
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
                    delete from os where id_os=:id_os
                ');
            
                $sql -> execute(array(
                    ':id_os'=> $_POST['id']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Ordem Excluída com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
       }
    }