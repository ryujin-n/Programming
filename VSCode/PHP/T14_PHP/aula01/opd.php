<?php
    $res = "";
    $resD="";
    
    if ($_POST) {
        $N1 = $_POST['txtN1'];
        $N2 = $_POST['txtN2'];
        $N3 = $_POST['txtN3'];
        $N4 = $_POST['txtN4'];
        

        $order =  ["$N1", "$N2", "$N3" , "$N4"];

        sort($order);

        $res = implode(" - ", $order);

        rsort($order);
        $resD = implode(" - ", $order);
    }
