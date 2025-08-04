<?php
   if ($_POST) {

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
           echo '<p>Cadastro Alterado com Sucesso</p>';
        }
    } catch (PDOException $th) {
        echo $th;
    }
   
   } 