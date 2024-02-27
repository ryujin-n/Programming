<?php

    $id="";
    $nome="";
    $nasc="";
    $data="";
    $cpf="";
    $logr="";
    $num="";
    $comp="";
    $cep="";
    $bai="";
    $cid="";
    $uf="";
    $tel="";
    $obs="";
    $sts="";

    if ($_POST) {
        include_once("conn.php");
        //cadastro

        if (isset($_POST["cad"])) {
            try {
        
                $sql = $conn -> prepare('
                    insert into funcionario
                        (nome_Funcionario,nasc_Funcionario,cpf_Funcionario,logradouro_Funcionario,numero_Funcionario,comp_funcionario,cep_Funcionario,bairro_Funcionario,cidade_Funcionario,uf_Funcionario,telefone1_Funcionario,obs_Funcionario)
                    values
                        (:nome_Funcionario,
                        :nasc_Funcionario,
                        :cpf_Funcionario,
                        :logradouro_Funcionario,
                        :numero_Funcionario,
                        :comp_funcionario,
                        :cep_Funcionario,
                        :bairro_Funcionario,
                        :cidade_Funcionario,
                        :uf_Funcionario,
                        :telefone1_Funcionario,
                        :obs_Funcionario)
                ');
            
                $sql -> execute(array(
                    ':nome_Funcionario' => $_POST['nome'],
                    ':nasc_Funcionario' =>$_POST['nasc'],
                    ':cpf_Funcionario' =>$_POST['cpf'],
                    ':logradouro_Funcionario' =>$_POST['logr'],
                    ':numero_Funcionario' =>$_POST['num'],
                    ':comp_funcionario' =>$_POST['comp'],
                    ':cep_Funcionario' => $_POST['cep'],
                    ':bairro_Funcionario' =>$_POST['bai'],
                    ':cidade_Funcionario' =>$_POST['cid'],
                    ':uf_Funcionario' =>$_POST['est'],
                    ':telefone1_Funcionario' =>$_POST['tel'],
                    ':obs_Funcionario' =>$_POST['obs'],
                ));  
            
                if ($sql -> rowCount() > 0) {
                    echo '<script>alert("Usuário Cadastrado com Sucesso")</script>';
                    header("Location:atv2.php?IDUsuario=".$conn->lastInsertId());
                }
            } catch (PDOException $th) {
                echo $th;
            }
           
           } 
            //pesquisa
            elseif (isset($_POST['pesq'])) {
                try {
                    $sql = $conn-> query('SELECT * FROM funcionario where ID_Funcionario='.$_POST['id'] );
                    if ($sql->rowCount() > 0) {
                        foreach ($sql as $line) {
    
                            $id= $line[0];
                            $nome= $line[1];
                            $nasc= $line[2];
                            $data= $line[3];
                            $data = substr($data, 0, 10);
                            $cpf= $line[4];
                            $logr= $line[5];
                            $num= $line[6];
                            $comp= $line[7];
                            $cep= $line[8];
                            $bai= $line[9];
                            $cid= $line[10];
                            $uf= $line[11];
                            $tel= $line[12];
                            $obs= $line[13];
                            $sts= $line[14];
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

                    $sql = $conn -> prepare('
                        UPDATE funcionario SET

                            nome_Funcionario = :nome_Funcionario,
                            nasc_Funcionario = :nasc_Funcionario,
                            cpf_Funcionario = :cpf_Funcionario,
                            logradouro_Funcionario = :logradouro_Funcionario,
                            numero_Funcionario = :numero_Funcionario,
                            comp_funcionario = :comp_funcionario,
                            cep_Funcionario = :cep_Funcionario,
                            bairro_Funcionario = :bairro_Funcionario,
                            cidade_Funcionario = :cidade_Funcionario,
                            uf_Funcionario = :uf_Funcionario,
                            telefone1_Funcionario = :telefone1_Funcionario,
                            obs_Funcionario = :obs_Funcionario,
                            status_Funcionario = :status_Funcionario

                         WHERE ID_Funcionario = :ID_Funcionario
                        
                    ');
                
                    $sql -> execute(array(
                        ':ID_Funcionario'=> $_POST['id'],
                        ':nome_Funcionario' => $_POST['nome'],
                        ':nasc_Funcionario' =>$_POST['nasc'],
                        ':cpf_Funcionario' =>$_POST['cpf'],
                        ':logradouro_Funcionario' =>$_POST['logr'],
                        ':numero_Funcionario' =>$_POST['num'],
                        ':comp_funcionario' =>$_POST['comp'],
                        ':cep_Funcionario' => $_POST['cep'],
                        ':bairro_Funcionario' =>$_POST['bai'],
                        ':cidade_Funcionario' =>$_POST['cid'],
                        ':uf_Funcionario' =>$_POST['est'],
                        ':telefone1_Funcionario' =>$_POST['tel'],
                        ':obs_Funcionario' =>$_POST['obs'],
                        ':status_Funcionario' => $_POST['sts']
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
                        delete from funcionario where ID_Funcionario=:ID_Funcionario
                    ');
                
                    $sql -> execute(array(
                        ':ID_Funcionario'=> $_POST['id']
                    ));  
                
                    if ($sql -> rowCount() > 0) {
                        echo '<script>alert("Usuário Excluído com Sucesso")</script>';
                    }
                } catch (PDOException $th) {
                    echo $th;
                }
           }
    }