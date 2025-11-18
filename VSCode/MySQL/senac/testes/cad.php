<?php
   if ($_POST) {
    try {
        include_once('conn.php');

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
           echo '<p>Cadastro Realizado com Sucesso</p>';
           echo '<p>ID Gerado'.$conn ->lastInsertId().'</p>';
        }
    } catch (PDOException $th) {
        echo $th;
    }
   
   } 