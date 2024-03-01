<?php

include_once("conn.php");
if($_POST)
{
    try
    {
        $sql = $conn->query("select * from usuario
             where 
             login_usuario ='".$_POST['user']."' 
             and 
             senha_usuario='".$_POST['pass']."'");
    
        if($sql->rowCount() == 1)
        {
            foreach($sql as $linha)
            {
                session_start();
                $_SESSION['idUsuarioLogin'] = $linha[0];
                $_SESSION['nomeUsuarioLogin'] = $linha[1];
                $_SESSION['loginUsuarioLogin'] = $linha[2];
                header('Location:initial.php');
            }
        }
        else
        {
            echo "<p>Usuário ou senha inválida</p>";
            echo "<p><a href='login.php'>Voltar</a></p>";
        }
        
    }
    catch(PDOException $erro)
    {
        echo $erro->getMessage();
    }
}
