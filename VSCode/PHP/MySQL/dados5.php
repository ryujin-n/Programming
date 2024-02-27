<?php

        $id="";
        $nome="";
        $data="";
        $obs="";
        $sts="";

        if ($_POST) {
            include_once('conn.php');
            //cadastro
        if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into localestoque
                        (nome_LocalEstoque,obs_LocalEstoque)
                    values
                        (:nome_LocalEstoque,:obs_LocalEstoque)
                ');
            
                $sql -> execute(array(
                    ':nome_LocalEstoque' => $_POST['nome'],
                    ':obs_LocalEstoque'=> $_POST['obs']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Armazém Cadastrado com Sucesso")</script>';
                    header("Location:atv5.php?IDUsuario=".$conn->lastInsertId());
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           } 
            //pesquisa
            elseif (isset($_POST['pesq'])) {
                try {
                    $sql = $conn-> query('SELECT * FROM localestoque where id_LocalEstoque='.$_POST['id'] );
                    if ($sql->rowCount() > 0) {
                        foreach ($sql as $line) {
    
                            $id=$line[0];
                            $nome=$line[1];
                            $data=$line[2];
                            $data = substr($data, 0, 10);
                            $obs=$line[3];
                            $sts=$line[4];
                        }
                    }
                    else {
                         echo '<script>alert("Armazém não encontrado")</script>';
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
                include_once('conn.php');

                $sql = $conn -> prepare('
                    update localestoque set

                        nome_LocalEstoque=:nome_LocalEstoque,
                        obs_LocalEstoque=:obs_LocalEstoque,
                        status_LocalEstoque=:status_LocalEstoque
                        
                    where id_LocalEstoque=:id_LocalEstoque
                    
                ');
            
                $sql -> execute(array(
                    ':id_LocalEstoque' => $_POST['id'],
                    ':nome_LocalEstoque' => $_POST['nome'],
                    ':obs_LocalEstoque'=> $_POST['obs'],
                    ':status_LocalEstoque'=> $_POST['sts']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Armazém Alterado com Sucesso")</script>';
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
                    delete from localestoque where id_LocalEstoque=:id_LocalEstoque
                ');
            
                $sql -> execute(array(
                    ':id_LocalEstoque'=> $_POST['id']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Armazém Excluído com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
       }
    }