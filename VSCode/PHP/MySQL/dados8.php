<?php

    $id="";
    $idp="";
    $idl="";
    $data="";
    $obs="";
    $sts="";


    if ($_POST) {
        include_once("conn.php");

          //cadastro
          if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into itemestoque
                        (id_produto_ItemEstoque,id_localEstoque_ItemEstoque,obs_ItemEstoque)
                    values
                        (:id_produto_ItemEstoque,:id_localEstoque_ItemEstoque,:obs_ItemEstoque)
                ');
            
                $sql -> execute(array(
                    ':id_produto_ItemEstoque' => $_POST['idp'],
                    ':id_localEstoque_ItemEstoque' => $_POST['idl'],
                    ':obs_ItemEstoque'=> $_POST['obs']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Estoque Cadastrado com Sucesso")</script>';
                    header("Location:atv8.php?IDUsuario=".$conn->lastInsertId());
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           }
           //pesquisa
           elseif (isset($_POST['pesq'])) {
            try {
                $sql = $conn-> query('SELECT * FROM itemestoque where id_ItemEstoque='.$_POST['id'] );
                if ($sql->rowCount() > 0) {
                    foreach ($sql as $line) {

                        $id=$line[0];
                        $idp=$line[1];
                        $idl=$line[2];
                        $data=$line[3];
                        $data=substr($data, 0, 10);
                        $obs=$line[4];
                        $sts=$line[5];
                    }
                }
                else {
                     echo '<script>alert("Estoque não encontrado")</script>';
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
                    UPDATE itemestoque SET
                        id_produto_ItemEstoque = :id_produto_ItemEstoque,
                        id_localEstoque_ItemEstoque = :id_localEstoque_ItemEstoque,
                        obs_ItemEstoque = :obs_ItemEstoque,
                        status_ItemEstoque = :status_ItemEstoque
                    WHERE id_ItemEstoque = :id_ItemEstoque
                ');
    
            $sql->execute(
                array(
                    ':id_ItemEstoque' => $_POST['id'],
                    ':id_produto_ItemEstoque' => $_POST['idp'],
                    ':id_localEstoque_ItemEstoque' => $_POST['idl'],
                    ':obs_ItemEstoque' => $_POST['obs'],
                    ':status_ItemEstoque' => $_POST['sts']
                )
            );
    
            if ($sql -> rowCount() > 0) {
                        echo '<script>alert("Estoque Alterado com Sucesso")</script>';
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
                    delete from itemestoque where id_ItemEstoque=:id_ItemEstoque
                ');
            
                $sql -> execute(array(
                    ':id_ItemEstoque'=> $_POST['id']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Estoque Excluída com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
       }

    }