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
                        (id_Produto_mov,id_funcionario_mov,qtde_mov,tipo_mov,obs_mov)
                    values
                        (:id_Produto_mov,:id_funcionario_mov,:qtde_mov,:tipo_mov,:obs_mov)
                ');
            
                $sql -> execute(array(
                    ':id_Produto_mov' => $_POST['idp'],
                    ':id_funcionario_mov' => $_POST['idf'],
                    ':qtde_mov'=> $_POST['qtde'],
                    ':tipo_mov'=> $_POST['tpo'],
                    ':obs_mov'=> $_POST['obs']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Movimentação Cadastrada com Sucesso")</script>';
                    header("Location:atv7.php?IDUsuario=".$conn->lastInsertId());
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           }

           //pesquisa
           elseif (isset($_POST['pesq'])) {
            try {
                $sql = $conn-> query('SELECT * FROM movimentacao where id_mov='.$_POST['id'] );
                if ($sql->rowCount() > 0) {
                    foreach ($sql as $line) {

                        $id=$line[0];
                        $idp=$line[1];
                        $idf=$line[2];
                        $qtde=$line[3];
                        $data=$line[4];
                        $data=substr($data, 0, 10);
                        $tpo=$line[5];
                        $obs=$line[6];
                        $sts=$line[7];
                    }
                }
                else {
                     echo '<script>alert("Movimentação não encontrada")</script>';
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
                UPDATE movimentacao SET
                    id_Produto_mov = :id_Produto_mov,
                    id_funcionario_mov = :id_funcionario_mov,
                    qtde_mov = :qtde_mov,
                    tipo_mov = :tipo_mov,
                    obs_mov = :obs_mov,
                    status_mov = :status_mov
                WHERE id_mov = :id_mov
            ');

        $sql->execute(
            array(
                ':id_mov' => $_POST['id'],
                ':id_Produto_mov' => $_POST['idp'],
                ':id_funcionario_mov' => $_POST['idf'],
                ':qtde_mov' => $_POST['qtde'],
                ':tipo_mov' => $_POST['tpo'],
                ':obs_mov' => $_POST['obs'],
                ':status_mov' => $_POST['sts']
            )
        );

        if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Movimentação Alterada com Sucesso")</script>';
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
                    delete from movimentacao where id_mov=:id_mov
                ');
            
                $sql -> execute(array(
                    ':id_mov'=> $_POST['id']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Movimentação Excluída com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
       }
    }