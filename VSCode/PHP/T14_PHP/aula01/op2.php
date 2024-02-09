<div class="container">
    <div class="row">
        <div class="col-sm-12">
            <?php 
                if ($_POST) {

                    $Prod = $_POST['txtProd'];
                    $Qtde = $_POST['txtQtde'];
                    $Val = $_POST['txtVal'];
                    $Pgto = $_POST['array'];
                    $total=0;

                    print_r($_POST);
                }
            ?>
        </div>
    </div>
</div>


