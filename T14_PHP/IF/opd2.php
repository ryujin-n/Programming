<?php

        $id = "";
        $name ="" ;
        $data = "";
        $street = "";
        $number = "";
        $postal = "";
        $comp = "";
        $nbd = "";
        $city = "";
        $state = "";
        $obs = "";
        $status = "";

   if ($_POST) {

        if (empty($_POST["id"]) || empty($_POST["nome"]) || empty($_POST["data"]) || empty($_POST["cep"]) || empty($_POST["rua"]) || empty($_POST["num"]) || empty($_POST["bai"]) || empty($_POST["cid"]) || empty($_POST["est"]) || empty($_POST["obs"]) || empty($_POST["sts"])) {
            $erro = "Por favor, preencha todos os campos obrigatórios.";
            
            $id = $_POST["id"];
            $name = $_POST["nome"];
            $data = $_POST["data"];
            $state = $_POST["est"];
            $postal = $_POST["cep"];
            $street = $_POST["rua"];
            $comp = $_POST["comp"];
            $number = $_POST["num"];
            $nbd = $_POST["bai"];
            $city = $_POST["cid"];
            $obs = $_POST["obs"];
            $status = $_POST["sts"];
        } else {
            $id = $_POST["id"];
            $name = $_POST["nome"];
            $data = $_POST["data"];
            $state = $_POST["est"];
            $postal = $_POST["cep"];
            $street = $_POST["rua"];
            $comp = $_POST["comp"];
            $number = $_POST["num"];
            $nbd = $_POST["bai"];
            $city = $_POST["cid"];
            $obs = $_POST["obs"];
            $status = $_POST["sts"];
        }
    }

   