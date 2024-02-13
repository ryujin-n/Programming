<div class="container">
    <div class="row">
        <div class="col-sm-12">
        <?php
            $diff = 0;
            $total = 0;

            if ($_POST) {
                $Prod = $_POST['prod'];
                $Qtde = $_POST['txtQtde'];
                $Val = $_POST['txtVal'];
                $Pgto = $_POST['pgto'];

                if ($Pgto == "px") {
                    $total = $Qtde * $Val;
                    $diff = $total - ($total * 0.05);
                }
                elseif ($Pgto == "dn") {
                    $total = $Qtde * $Val;
                    $diff = $total - ($total * 0.1);
                }
                elseif ($Pgto == "db") {
                    $total = $Qtde * $Val;
                    $diff = $Qtde * $Val;
                }
                elseif ($Pgto == "cr") {
                    $total = $Qtde * $Val;
                    $diff = $total + ($total * 0.08);
                }
                elseif ($Pgto == "bl") {
                    $total = $Qtde * $Val;
                    $diff = $total + (($total * 0.1)+5);
                }
            }

            ?>
        </div>
    </div>
</div>


