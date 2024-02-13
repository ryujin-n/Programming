<!-- Desafio 02
 Criar um sistema que faça a validação de dados de uma tela de cadastro de clientes
ID, nome, data nascimento, rua, numero, complemento, cep, bairro, cidade, estado, pais, observação, status

Não apagar os dados caso o valor não seja preenchido -->



<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro</title>
    <link rel="stylesheet" href="css/bootstrap.css">
</head>

<body>
    <div class="container">
        <form action="" method="post" class="form-control w-50 mx-auto">
            <div class="row">
                <div class="col-sm-12">
                    <b style="text-align:center;">
                        <h2>Cadastro</h2>
                    </b>
                    <hr>
                    <br>
                </div>

                <div class="col-sm-6">
                    <p>
                        <label for="txtID" class="ms-1">ID</label>
                    </p>
                    <p>
                        <input type="number" name="txtID" id="txtID" class="form-control w-25" value="" disabled>
                    </p>
                    <br>
                </div>
                
                <div class="col-sm-6">
                    <p>
                        <label for="txtStat" class="ms-1">Status</label>
                    </p>
                    <p>
                        <input type="text" name="txtStat" id="txtStat" class="form-control" value="" disabled>
                    </p>
                    <br>
                </div>


            </div>

            <div class="row">
                <div class="col-sm-6">
                    <p>
                        <input type="text" name="txtName" id="txtID" class="form-control" placeholder="Nome Completo">
                    </p>
                </div>
                <div class="col-sm-6">
                    <p>
                        <input type="text" name="txtID" id="txtNasc" class="form-control"
                            placeholder="Data de Nascimento">
                    </p>
                    <br>

                </div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <p>
                        <input type="text" name="txtRua" id="txtID" class="form-control" placeholder="Rua">
                    </p>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-6">
                    <p>
                        <input type="text" name="txtID" id="txtComp" class="form-control" placeholder="Complemento">
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <p>
                        <input type="text" name="txtID" id="txtCep" class="form-control" placeholder="CEP">
                    </p>
                </div>
                <div class="col-sm-6">
                    <p>
                        <input type="text" name="txtID" id="txtBai" class="form-control" placeholder="Bairro">
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <p>
                        <input type="text" name="txtID" id="txtCid" class="form-control" placeholder="Cidade">
                    </p>
                </div>
                <div class="col-sm-6">
                    <p>
                        <select name="estados" class="form-control">
                            <option value=""> -- Estado --</option>
                            <option value="ac">Acre</option>
                            <option value="al">Alagoas</option>
                            <option value="ap">Amapá</option>
                            <option value="am">Amazonas</option>
                            <option value="ba">Bahia</option>
                            <option value="ce">Ceará</option>
                            <option value="df">Distrito Federal</option>
                            <option value="es">Espírito Santo</option>
                            <option value="go">Goiás</option>
                            <option value="ma">Maranhão</option>
                            <option value="mt">Mato Grosso</option>
                            <option value="ms">Mato Grosso do Sul</option>
                            <option value="mg">Minas Gerais</option>
                            <option value="pa">Pará</option>
                            <option value="pb">Paraíba</option>
                            <option value="pr">Paraná</option>
                            <option value="pe">Pernambuco</option>
                            <option value="pi">Piauí</option>
                            <option value="rj">Rio de Janeiro</option>
                            <option value="rn">Rio Grande do Norte</option>
                            <option value="rs">Rio Grande do Sul</option>
                            <option value="ro">Rondônia</option>
                            <option value="rr">Roraima</option>
                            <option value="sc">Santa Catarina</option>
                            <option value="sp">São Paulo</option>
                            <option value="se">Sergipe</option>
                            <option value="to">Tocantins</option>
                        </select>
                    </p>
                </div>

                <div class="row">
                    <div class="col-sm-6">
                        <p>
                            <select name="paises" class="form-control">
                                <option value=""> -- País  -- </option>
                                <option value="af">Afeganistão</option>
                                <option value="ax">Aland, Ilhas</option>
                                <option value="al">Albânia</option>
                                <option value="dz">Argélia</option>
                                <option value="as">Samoa Americana</option>
                                <option value="ad">Andorra</option>
                                <option value="ao">Angola</option>
                                <option value="ai">Anguilla</option>
                                <option value="aq">Antártida</option>
                                <option value="ag">Antígua e Barbuda</option>
                                <option value="ar">Argentina</option>
                                <option value="am">Armênia</option>
                                <option value="aw">Aruba</option>
                                <option value="au">Austrália</option>
                                <option value="at">Áustria</option>
                                <option value="az">Azerbaijão</option>
                                <option value="bs">Bahamas</option>
                                <option value="bh">Bahrein</option>
                                <option value="bd">Bangladesh</option>
                                <option value="bb">Barbados</option>
                                <option value="by">Belarus</option>
                                <option value="be">Bélgica</option>
                                <option value="bz">Belize</option>
                                <option value="bj">Benin</option>
                                <option value="bm">Bermudas</option>
                                <option value="bt">Butão</option>
                                <option value="bo">Bolívia</option>
                                <option value="ba">Bósnia e Herzegovina</option>
                                <option value="bw">Botsuana</option>
                                <option value="bv">Bouvet, Ilha</option>
                                <option value="br">Brasil</option>
                                <option value="vg">Ilhas Virgens Britânicas</option>
                                <option value="bn">Brunei</option>
                                <option value="bg">Bulgária</option>
                                <option value="bf">Burkina Faso</option>
                                <option value="bi">Burundi</option>
                                <option value="cv">Cabo Verde</option>
                                <option value="kh">Camboja</option>
                                <option value="cm">Camarões</option>
                                <option value="ca">Canadá</option>
                                <option value="ky">Ilhas Caiman</option>
                                <option value="cf">República Centro-Africana</option>
                                <option value="td">Chade</option>
                                <option value="cl">Chile</option>
                                <option value="cn">China</option>
                                <option value="cx">Ilha Christmas</option>
                                <option value="cc">Cocos, Ilhas</option>
                                <option value="co">Colômbia</option>
                                <option value="km">Comores</option>
                                <option value="cd">Congo, República Democrática do</option>
                                <option value="cg">Congo, República do</option>
                                <option value="ck">Ilhas Cook</option>
                                <option value="cr">Costa Rica</option>
                                <option value="ci">Costa do Marfim</option>
                                <option value="hr">Croácia</option>
                                <option value="cu">Cuba</option>
                                <option value="cw">Curaçao</option>
                                <option value="cy">Chipre</option>
                                <option value="cz">República Tcheca</option>
                                <option value="dk">Dinamarca</option>
                                <option value="dj">Djibuti</option>
                                <option value="dm">Dominica</option>
                                <option value="do">República Dominicana</option>
                                <option value="tl">Timor-Leste</option>
                                <option value="ec">Equador</option>
                                <option value="eg">Egito</option>
                                <option value="sv">El Salvador</option>
                                <option value="gq">Guiné Equatorial</option>
                                <option value="er">Eritreia</option>
                                <option value="ee">Estônia</option>
                                <option value="et">Etiópia</option>
                                <option value="fk">Ilhas Malvinas</option>
                                <option value="fo">Ilhas Faroe</option>
                                <option value="fj">Fiji</option>
                                <option value="fi">Finlândia</option>
                                <option value="fr">França</option>
                                <option value="gf">Guiana Francesa</option>
                                <option value="pf">Polinésia Francesa</option>
                                <option value="tf">Terras Austrais Francesas</option>
                                <option value="ga">Gabão</option>
                                <option value="gm">Gâmbia</option>
                                <option value="ge">Geórgia</option>
                                <option value="gh">Gana</option>
                                <option value="gi">Gibraltar</option>
                                <option value="gr">Grécia</option>
                                <option value="gl">Groenlândia</option>
                                <option value="gd">Granada</option>
                                <option value="gp">Guadalupe</option>
                                <option value="gu">Guam</option>
                                <option value="gt">Guatemala</option>
                                <option value="gg">Guernsey</option>
                                <option value="gn">Guiné</option>
                                <option value="gw">Guiné-Bissau</option>
                                <option value="gy">Guiana</option>
                                <option value="ht">Haiti</option>
                                <option value="hm">Ilha Heard e Ilhas McDonald</option>
                                <option value="hn">Honduras</option>
                                <option value="hk">Hong Kong</option>
                                <option value="hu">Hungria</option>
                                <option value="is">Islândia</option>
                                <option value="in">Índia</option>
                                <option value="id">Indonésia</option>
                                <option value="ir">Irã</option>
                                <option value="iq">Iraque</option>
                                <option value="ie">Irlanda</option>
                                <option value="im">Ilha de Man</option>
                                <option value="il">Israel</option>
                                <option value="it">Itália</option>
                                <option value="jm">Jamaica</option>
                                <option value="jp">Japão</option>
                                <option value="je">Jersey</option>
                                <option value="jo">Jordânia</option>
                                <option value="kz">Cazaquistão</option>
                                <option value="ke">Quênia</option>
                                <option value="ki">Kiribati</option>
                                <option value="kw">Kuwait</option>
                                <option value="kg">Quirguistão</option>
                                <option value="la">Laos</option>
                                <option value="lv">Letônia</option>
                                <option value="lb">Líbano</option>
                                <option value="ls">Lesoto</option>
                                <option value="lr">Libéria</option>
                                <option value="ly">Líbia</option>
                                <option value="li">Liechtenstein</option>
                                <option value="lt">Lituânia</option>
                                <option value="lu">Luxemburgo</option>
                                <option value="mo">Macau</option>
                                <option value="mk">Macedônia</option>
                                <option value="mg">Madagascar</option>
                                <option value="mw">Malawi</option>
                                <option value="my">Malásia</option>
                                <option value="mv">Maldivas</option>
                                <option value="ml">Mali</option>
                                <option value="mt">Malta</option>
                                <option value="mh">Ilhas Marshall</option>
                                <option value="mq">Martinica</option>
                                <option value="mr">Mauritânia</option>
                                <option value="mu">Maurício</option>
                                <option value="yt">Mayotte</option>
                                <option value="mx">México</option>
                                <option value="fm">Micronésia</option>
                                <option value="md">Moldávia</option>
                                <option value="mc">Mônaco</option>
                                <option value="mn">Mongólia</option>
                                <option value="me">Montenegro</option>
                                <option value="ms">Montserrat</option>
                                <option value="ma">Marrocos</option>
                                <option value="mz">Moçambique</option>
                                <option value="mm">Myanmar</option>
                                <option value="na">Namíbia</option>
                                <option value="nr">Nauru</option>
                                <option value="np">Nepal</option>
                                <option value="nc">Nova Caledônia</option>
                                <option value="nz">Nova Zelândia</option>
                                <option value="ni">Nicarágua</option>
                                <option value="ne">Níger</option>
                                <option value="ng">Nigéria</option>
                                <option value="nu">Niue</option>
                                <option value="nf">Ilha Norfolk</option>
                                <option value="kp">Coreia do Norte</option>
                                <option value="mp">Ilhas Marianas do Norte</option>
                                <option value="no">Noruega</option>
                                <option value="om">Omã</option>
                                <option value="pk">Paquistão</option>
                                <option value="pw">Palau</option>
                                <option value="ps">Palestina</option>
                                <option value="pa">Panamá</option>
                                <option value="pg">Papua-Nova Guiné</option>
                                <option value="py">Paraguai</option>
                                <option value="pe">Peru</option>
                                <option value="ph">Filipinas</option>
                                <option value="pn">Ilhas Pitcairn</option>
                                <option value="pl">Polônia</option>
                                <option value="pt">Portugal</option>
                                <option value="pr">Porto Rico</option>
                                <option value="qa">Catar</option>
                                <option value="re">Reunião</option>
                                <option value="ro">Romênia</option>
                                <option value="ru">Rússia</option>
                                <option value="rw">Ruanda</option>
                                <option value="bl">São Bartolomeu</option>
                                <option value="sh">Santa Helena</option>
                                <option value="kn">São Cristóvão e Névis</option>
                                <option value="lc">Santa Lúcia</option>
                                <option value="mf">São Martinho</option>
                                <option value="pm">São Pedro e Miquelon</option>
                                <option value="vc">São Vicente e Granadinas</option>
                                <option value="ws">Samoa</option>
                                <option value="sm">San Marino</option>
                                <option value="st">São Tomé e Príncipe</option>
                                <option value="sa">Arábia Saudita</option>
                                <option value="sn">Senegal</option>
                                <option value="rs">Sérvia</option>
                                <option value="sc">Seicheles</option>
                                <option value="sl">Serra Leoa</option>
                                <option value="sg">Singapura</option>
                                <option value="sx">Sint Maarten</option>
                                <option value="sk">Eslováquia</option>
                                <option value="si">Eslovênia</option>
                                <option value="sb">Ilhas Salomão</option>
                                <option value="so">Somália</option>
                                <option value="za">África do Sul</option>
                                <option value="gs">Geórgia do Sul e Ilhas Sandwich do Sul</option>
                                <option value="kr">Coreia do Sul</option>
                                <option value="ss">Sudão do Sul</option>
                                <option value="es">Espanha</option>
                                <option value="lk">Sri Lanka</option>
                                <option value="sd">Sudão</option>
                                <option value="sr">Suriname</option>
                                <option value="sj">Svalbard e Jan Mayen</option>
                                <option value="sz">Suazilândia</option>
                                <option value="se">Suécia</option>
                                <option value="ch">Suíça</option>
                                <option value="sy">Síria</option>
                                <option value="tw">Taiwan</option>
                                <option value="tj">Tajiquistão</option>
                                <option value="tz">Tanzânia</option>
                                <option value="th">Tailândia</option>
                                <option value="tg">Togo</option>
                                <option value="tk">Tokelau</option>
                                <option value="to">Tonga</option>
                                <option value="tt">Trinidad e Tobago</option>
                                <option value="tn">Tunísia</option>
                                <option value="tr">Turquia</option>
                                <option value="tm">Turcomenistão</option>
                                <option value="tc">Ilhas Turks e Caicos</option>
                                <option value="tv">Tuvalu</option>
                                <option value="ug">Uganda</option>
                                <option value="ua">Ucrânia</option>
                                <option value="ae">Emirados Árabes Unidos</option>
                                <option value="gb">Reino Unido</option>
                                <option value="us">Estados Unidos</option>
                                <option value="um">Estados Unidos Menores Distantes</option>
                                <option value="uy">Uruguai</option>
                                <option value="uz">Uzbequistão</option>
                                <option value="vu">Vanuatu</option>
                                <option value="va">Vaticano</option>
                                <option value="ve">Venezuela</option>
                                <option value="vn">Vietnã</option>
                                <option value="wf">Wallis e Futuna</option>
                                <option value="eh">Saara Ocidental</option>
                                <option value="ye">Iêmen</option>
                                <option value="zm">Zâmbia</option>
                                <option value="zw">Zimbábue</option>
                            </select>

                            <br>
                            <hr>

                        </p>
                    </div>
                </div>

                <div class="row">
                    <p>
                        <label for="txtObs">Observações</label>
                    </p>
                    <p>
                        <textarea name="txtObs" id="txtObs" cols="30" rows="5" class="form-control"></textarea>
                    </p>
                </div>

                <div class="row">
                    <div class="col-sm-6">
                        <button class="btn btn-success mt-3 mb-3" id="btoOK" name="btoOK" formaction="opd2.php">OK</button>
                        <a href="ds2.php" class="btn btn-danger">Apagar</a>
                    </div>
                   
                </div>
            </div>
        </form>
    </div>




    <script src="js/bootstrap.js"></script>
</body>

</html>