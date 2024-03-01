    <div class="col-sm-12 mt-5">
        <nav class="navbar navbar-expand-lg navbar-light bg-body-tertiary">
            <div class="container">
                <button data-mdb-collapse-init class="navbar-toggler" type="button" data-mdb-target="#navbarButtonsExample"
                aria-controls="navbarButtonsExample" aria-expanded="false" aria-label="Toggle navigation">
                <i class="fas fa-bars"></i>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarButtonsExample">
                <ul class="navbar-nav mx-auto">
                        <li class="nav-item">
                            <h5>Cadastro Legal do milos</h5>
                        </li>
                    </ul>
                    <div class="p-3">
                    <p>ID: <?=$idUsuarioSessao?><br>
                        Nome: <?=$nomeUsuarioSessao?><br>
                        Login: <?=$loginUsuarioSessao?><br></p>
                        <a href="logoff.php" class="btn btn-danger">Sair</a>
                        <a data-mdb-ripple-init class="btn btn-dark px-3" href="https://github.com/mdbootstrap/mdb-ui-kit"
                        role="button"><i class="fab fa-github"></i></a>
                    </div>
                    <div class="d-flex align-items-center">
                      
                    </div>
                </div>
            </div>
        </nav>
    </div>
    <script src="https://kit.fontawesome.com/9d5d0bd5f5.js" crossorigin="anonymous"></script>
    <script src="js/bootstrap.js"></script>