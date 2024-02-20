<!DOCTYPE html>
<html lang="pt-br">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tabela de Investimento</title>
  <link rel="stylesheet" href="css/bootstrap.css">
  <link rel="stylesheet" href="css/style.css">
</head>

<body>
  <div class="container mt-5">
    <form action="" class="form-control w-50 mx-auto" method="post">
      <div class="row">
        <div class="col-sm-12">
          <b style="text-align:center;">
            <h2>Calculadora de Investimentos</h2>
          </b>
          <hr>
          <br>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6">
          <p>
            <input type="number" class="form-control" name="v1" placeholder="Valor Inicial">
          </p>
        </div>
        <div class="col-sm-6">
          <p>
            <input type="number" class="form-control" name="inv" placeholder="Valor Aplicado">
          </p>
        </div>
        <div class="col-sm-4">
          <p>
            <input type="number" class="form-control" name="time" placeholder="Duração (Anos)">
          </p>

        </div>
        <div class="col-sm-4">
          <p>
            <input type="number" class="form-control" name="inf" placeholder="Juros (%)">
          </p>

        </div>
      </div>

      <p>
        <button class="btn btn-success" name="w">OK</button>
        <a href="tabelinha.php" class="btn btn-danger">Limpar</a>
      </p>

      <hr>

      <div class="row">
        <div class="col-sm-12">
          <b style="text-align:center;">
            <u>
              <h2>Valor Final</h2>
            </u>
            <br>
          </b>
        </div>

        <div class="col-sm-12">
          <input type="number" class="form-control w-50 mx-auto h-75" name="res" disabled value="<?= "" ?>">
          <br>
        </div>
      </div>
    </form>

    <div class="row mt-5">
      <div class="col">
        <div class="tabela-customizada"></div>
      </div>
    </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="mt-5 mb-4 text-center">
          <h1>Tabela de Investimento</h1>
        </div>
        <hr>

        <form action="" class="form-control mb-5">
          <div class="col-12">
            <table class="table table-striped table-bordered ">
              <thead>
                <tr>
                  <th>Janeiro</th>
                  <th>Fevereiro</th>
                  <th>Março</th>
                  <th>Abril</th>
                  <th>Maio</th>
                  <th>Junho</th>
                  <th>Julho</th>
                  <th>Agosto</th>
                  <th>Setembro</th>
                  <th>Outubro</th>
                  <th>Novembro</th>
                  <th>Dezembro</th>
                </tr>
              </thead>

              <tbody>

                <?php

                $val = isset($_POST["v1"]) ? $_POST["v1"] : 0;
                $inv = isset($_POST["inv"]) ? $_POST["inv"] : 0;
                $time = isset($_POST["time"]) ? $_POST["time"] : 0;
                $infl = isset($_POST["inf"]) ? $_POST["inf"] : 0;

                $tr = 0;

                if ($_POST) {

                  for ($i = 1; $i <= $time; $i++) {
                    echo "<tr>";
                    for ($j = 1; $j <= 12; $j++) {
                      echo "<td>---</td>";
                    }
                    echo "</tr>";
                  }

                }
                ?>

              </tbody>
            </table>
          </div>
        </form>
      </div>
    </div>
  </div>

  <script src="js/bootstrap.js"></script>
</body>

</html>