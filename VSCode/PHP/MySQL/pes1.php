<?php


if(!isset($_POST['action']) && !isset($_GET['IDUsuario']))
{

    echo 'passou por aq';
    return;
}


if($_POST or $_GET)
{
    include_once('conn.php');

    $idUsuario="";

    
    if(isset($_POST['action']))
    {
        if($_POST['action']=='pes')
        {
            $idUsuario=$_POST['id'];
        }
        else
        {
            return;
        }
    }
    elseif(isset($_GET['IDUsuario']))
    {        
        $idUsuario=$_GET['IDUsuario'];
        echo 'passou por aq2';
    }

    try
    {
        echo $idUsuario;

        $sql = $conn->query('select * from usuario where id_usuario='.$idUsuario);

        if($sql->rowCount()>0)
        {
            foreach($sql as $linha)
            {
                $ID=$linha[0];
                $Nome=$linha[1];
                $Login=$linha[2];
                $Senha= $linha[3];
                $Data=$linha[4];
                $Data = substr($Data, 0, 10);
                $Obs=$linha[5];
                $Status=$linha[6];
                $Img=$linha[7];
            }
        }else{
            echo '<script>alert("Usuário não encontrado")</script>';
        }
        
    }
    catch(PDOException $erro)
    {
        echo $erro->getMessage();
    }   
}
