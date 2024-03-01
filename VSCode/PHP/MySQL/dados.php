<?php

        $ID="";
        $Nome="";
        $Login="";
        $Senha="";
        $Data="";
        $Obs="";
        $img="";
        $Status="";
        
    if ($_POST) {
        include_once('conn.php');
        $arquivo = $_FILES['img'];
        //cadastro
        if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into usuario
                        (nome_usuario,login_usuario,senha_usuario,obs_usuario,img_usuario)
                    values
                        (:nome_usuario,:login_usuario,:senha_usuario,:obs_usuario,:img_usuario)
                ');
            
                $sql -> execute(array(
                    ':nome_usuario' => $_POST['nome'],
                    ':login_usuario'=> $_POST['user'],
                    ':senha_usuario'=> $_POST['senha'],
                    ':obs_usuario'=> $_POST['obs'],
                    ':img_usuario'=> $arquivo['name']
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Usuário Cadastrado com Sucesso")</script>';

                    $pasta = 'src/'.$conn->lastInsertId().'/';
            
                    if(!file_exists($pasta))
                    {
                        mkdir($pasta);
                    }
        
                    $foto = $pasta.$arquivo['name'];
        
                    move_uploaded_file($arquivo['tmp_name'],$foto);

                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           } 
           //pesquisa
           elseif(isset($_POST['pesq']) or isset($_GET['IDUsuario']))
           {
           
               $idUsuario="";
           
               if(isset($_POST['pesq']))
               {
                   $idUsuario=$_POST['id'];
               }
               elseif(isset($_GET['IDUsuario']))
               {
                   $idUsuario=$_GET['IDUsuario'];
               }
           
               try
               {
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
                           $img=$linha[6];
                           $Status=$linha[7];
                       }
                   }else{
                       echo '<script>alert("Usuário não encontrado")</script>';
                       $mensagem = "Usuário não encontado";
                   }
                   
               }
               catch(PDOException $erro)
               {
                   echo $erro->getMessage();
               }   
           }
           //alterar
           elseif (isset($_POST["alt"])) {
            try {
                include_once('conn.php');
        
                $arquivo = $_FILES['img'];
        
                $sql = $conn->prepare('
                    UPDATE usuario SET
                        nome_usuario=:nome_usuario,
                        login_usuario=:login_usuario,
                        senha_usuario=:senha_usuario,
                        obs_usuario=:obs_usuario,
                        img_usuario=:img_usuario, 
                        status_usuario=:status_usuario
                    WHERE id_usuario=:id_usuario
                ');
        
                $sql->execute(array(
                    ':id_usuario' => $_POST['id'],
                    ':nome_usuario' => $_POST['nome'],
                    ':login_usuario' => $_POST['user'],
                    ':senha_usuario' => $_POST['senha'],
                    ':obs_usuario' => $_POST['obs'],
                    ':img_usuario' => $arquivo['name'], // Usando o nome do arquivo enviado
                    ':status_usuario' => $_POST['sts']
                ));
        
                if ($sql->rowCount() > 0) {
                    echo '<script>alert("Usuário Alterado com Sucesso")</script>';
        
                    $pasta = 'src/' . $_POST['id'] . '/'; // Usando o ID do usuário para criar a pasta
        
                    if (!file_exists($pasta)) {
                        mkdir($pasta);
                    }
        
                    $foto = $pasta . $arquivo['name']; // Caminho completo para a imagem
        
                    move_uploaded_file($arquivo['tmp_name'], $foto);
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