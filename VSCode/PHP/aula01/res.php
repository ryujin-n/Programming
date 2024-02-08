<div class="container">
    <div class="row">
        <div class="col-sm-12">
        <?php
                $sts = "";
                $media = 0;
                $color = "";

                if($_POST && isset($_POST['txtN1']) && isset($_POST['txtN2']) && isset($_POST['txtN3']) && isset($_POST['txtN4'])) {
                    $N1 = $_POST['txtN1'];
                    $N2 = $_POST['txtN2'];
                    $N3 = $_POST['txtN3'];
                    $N4 = $_POST['txtN4'];
                    
                    $media = (intval($N1) + intval($N2) + intval($N3) + intval($N4)) / 4;

                    if($media > 7) {
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
