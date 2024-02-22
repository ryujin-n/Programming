<?php

        $ID="";
        $Nome="";
        $Login="";
        $Senha="";
        $Data="";
        $Obs="";
        $Status="";
        
    if ($_POST) {
        
        include_once('conn.php');
        

        //cadastro
        if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into usuario
                        (nome_usuario,login_usuario,senha_usuario,obs_usuario)
                    values
                        (:nome_usuario,:login_usuario,:senha_usuario,:obs_usuario)
                ');
            
                $sql -> execute(array(
                    ':nome_usuario' => $_POST['nome'],
                    ':login_usuario'=> $_POST['user'],
                    ':senha_usuario'=> $_POST['senha'],
                    ':obs_usuario'=> $_POST['obs']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Usuário Excluído com Sucesso")</script>';
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           } 
           //pesquisa
           elseif (isset($_POST['pesq'])) {
            try {
                $sql = $conn-> query('SELECT * FROM usuario where id_usuario='.$_POST['id'] );
                if ($sql->rowCount() > 0) {
                    foreach ($sql as $line) {

                        $ID=$line[0];
                        $Nome=$line[1];
                        $Login=$line[2];
                        $Senha= $line[3];
                        $Data=$line[4];
                        $Data = substr($Data, 0, 10);
                        $Obs=$line[5];
                        $Status=$line[6];
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
                    include_once('conn.php');

                    $sql = $conn -> prepare('
                        update usuario set

                            nome_usuario=:nome_usuario,
                            login_usuario=:login_usuario,
                            senha_usuario=:senha_usuario,
                            obs_usuario=:obs_usuario,
                            status_usuario=:status_usuario
                            
                        where id_usuario=:id_usuario
                        
                    ');
                
                    $sql -> execute(array(
                        ':id_usuario' => $_POST['id'],
                        ':nome_usuario' => $_POST['nome'],
                        ':login_usuario'=> $_POST['user'],
                        ':senha_usuario'=> $_POST['senha'],
                        ':obs_usuario'=> $_POST['obs'],
                        ':status_usuario'=> $_POST['sts']
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
                        delete from usuario where id_usuario=:id_usuario
                    ');
                
                    $sql -> execute(array(
                        ':id_usuario'=> $_POST['id']
                    ));  
                
                    if ($sql -> rowCount() > 0) {
                        echo '<script>alert("Usuário Excluído com Sucesso")</script>';
                    }
                } catch (PDOException $th) {
                    echo $th;
                }
           }
    }