<div class="container">
    <div class="row">
        <div class="col-sm-12">
            <?php

                $N1 = $_POST['txtN1'];
                $N2 = $_POST['txtN2'];
                $N3 = $_POST['txtN3'];
                $N4 = $_POST['txtN4'];
                $sts = $_POST['txtStat'];
                $media = 0;
                $color =0;

                if($_POST){

                   $media = (intval($N1) + intval($N2) + intval($N3) + intval($N4))/4;

                   if($media > 7){

                    $sts = "Aprovado";

                   }
                   elseif ($media < 5) {
                    $sts = "Reprovado";
                   }
                   else{
                    $sts = "Exame";
                   }

                }

                echo "<h2>$sts</h2>"
            
            ?>
        </div>
    </div>
</div>
