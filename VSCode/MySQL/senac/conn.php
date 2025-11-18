<?php

$host="localhost";
$db="t14_MiniProjeto";
$user="root";
$pass="";


try {
    $conn = new PDO("mysql:dbname=$db;host=$host", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $conn->exec("set names utf8");
} catch (PDOException $error) {
    echo  $error->getMessage();
}