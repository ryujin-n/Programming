<div class="container">
    <div class="row">
        <div class="col-sm-12">
            <?php
                $N1 = $_POST['txtN1'];
                $N2 = $_POST['txtN2'];
                $total = 0;

                if($_POST){
                    if(isset($_POST['btoMais'])){

                        $total = $N1 + $N2;
                    }
                    elseif(isset($_POST['btoMenos'])){

                        $total = $N1 - $N2;
                    }
                    elseif(isset($_POST['btoVezes'])){

                        $total = $N1 * $N2;
                    }
                    elseif(isset($_POST['btoDividir'])){

                        $total = $N1 / $N2;
                    }
                    else{
                        echo "Erro";
                    }
                }

                echo "<h2>$total</h2>";
            ?>
        </div>
    </div>
</div>