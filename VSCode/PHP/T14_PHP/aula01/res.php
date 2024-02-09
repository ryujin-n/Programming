<div class="container">
    <div class="row">
        <div class="col-sm-12">
        <?php
                $sts = "";
                $media = 0;
                $color = "";
                $n1=0;
                $n2= 0;
                $n3= 0;
                $n4= 0;

                if($_POST) {
                    $n1 = $_POST['txtN1'];
                    $n2 = $_POST['txtN2'];
                    $n3 = $_POST['txtN3'];
                    $n4 = $_POST['txtN4'];
                    
                    $media = ($n1 + $n2 + $n3 + $n4)/4;


                    if($media >= 7) {
                        $sts = "Aprovado :)";
                        $color = "green";
                    } elseif ($media < 5) {
                        $sts = "Reprovado :(";
                        $color = "red";
                    } else {
                        $sts = "Exame :/";
                        $color = "gold";
                    }
                    
                }
            ?>
        </div>
    </div>
</div>
