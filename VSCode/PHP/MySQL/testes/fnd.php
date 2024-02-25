<?php

if ($_POST)
{
    include_once("conn.php");

    try {
        $sql = $conn-> query('SELECT * FROM usuario where id_usuario='.$_POST['id'] );
        if ($sql->rowCount() > 0) {
            foreach ($sql as $line) {
                echo"
                <p>ID: ".$line[0]."</p>
                <p>Nome: ".$line[1]."</p>
                <p>Login: ".$line[2]."</p>
                <p>Senha: ".$line[3]."</p>
                <p>Data : ".$line[4]."</p>
                <p>Obs : ".$line[5]."</p>
                <p>Status : ".$line[6]."</p>
                ";
            }
        }
        else {
            echo "Usuário não encontrado :c";
        }
    }
     catch (PDOException $th)
    {
        echo $th;
    }
}