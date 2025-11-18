<?php
   if ($_POST) {

    try {
        include_once('conn.php');

        $sql = $conn -> prepare('
            delete from usuario where id_usuario=:id_usuario
        ');
    
        $sql -> execute(array(
            ':id_usuario'=> $_POST['id']
        ));  
    
        if ($sql -> rowCount() > 0) {
           echo '<p>Cadastro Excluido com Sucesso</p>';
        }
    } catch (PDOException $th) {
        echo $th;
    }
   
   } 