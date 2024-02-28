<!DOCTYPE html>
<html lang="br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tela Inicial</title>
        <link rel="stylesheet" href="css/bootstrap.css">
        <link rel="stylesheet" href="css/style.css">
        <script src="js/bootstrap.js"></script>
        <script src="https://kit.fontawesome.com/9d5d0bd5f5.js" crossorigin="anonymous"></script>

</head>
<body>

    <div class="container">
        <div class="row">
            <?php include_once("header&footer/header.php"); ?>
        </div>
    </div>
    <div class="container mb-3">
        <div class="row">
            <div class="col-sm-2">
                <?php include_once("menu.php");?>
            </div>
            <div class="col-sm-10">
                <?php
                if(isset($_GET['tela']))
                {
                    $tela = $_GET['tela'];

                    if($tela=='usuario')
                    {
                        include_once("atv1.php"); 
                    }
                    elseif ($tela=='func') {
                        
                        include_once("atv2.php"); 
                    }
                    elseif ($tela=='forn') {

                        include_once("atv3.php"); 
                    }
                    elseif ($tela=='prod') {

                        include_once("atv4.php"); 
                    }
                    elseif ($tela=='armazem') {

                        include_once("atv5.php"); 
                    }
                    elseif ($tela=='os') {

                        include_once("atv6.php"); 
                    }
                    elseif ($tela=='mov') {

                        include_once("atv7.php"); 
                    }
                    elseif ($tela=='estoque') {

                        include_once("atv8.php"); 
                    }
                    
                }
                else
                {
                    include_once("home.php"); 
                }
                ?>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
        <?php include_once("header&footer/footer.php"); ?>
        </div>
    </div>
    
</body>
</html>