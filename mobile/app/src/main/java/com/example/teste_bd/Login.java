package com.example.teste_bd;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


public class Login extends AppCompatActivity implements View.OnClickListener {
    EditText txtEmail, txtSenha;
    Button   btAcessar;


    TextView txtCadastroLink;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);


        txtEmail = findViewById(R.id.txtLogEmail);
        txtSenha = findViewById(R.id.txtLogSenha);
        btAcessar = findViewById(R.id.btEntrar);
        txtCadastroLink = findViewById(R.id.txtCadastroLink);


        btAcessar.setOnClickListener(this);
        txtCadastroLink.setOnClickListener(this);


    }


    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.btEntrar) {


            String msg;
            if (txtEmail.getText().length() == 0) {
                msg = "O campo de Email deve ser preenchido!";
                Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_LONG).show();
            } else {
                if (txtSenha.getText().length() == 0) {
                    msg = "O campo de Senha deve ser preenchido!";
                    Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_LONG).show();
                } else {
                    BancoControllerUsuarios bd = new BancoControllerUsuarios(getBaseContext());


                    Cursor dados = bd.ConsultaLogin(txtEmail.getText().toString(),
                            txtSenha.getText().toString());


                    if (dados.moveToFirst()) {
                        Intent tela = new Intent(this, Menu.class);
                        startActivity(tela);
                        finish();
                    } else {
                        msg = "O E-mail/Senha não estão cadastrados, cadastre-se!";
                        Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_LONG).show();
                    }
                }
            }
        }
        if (v.getId() == R.id.txtCadastroLink) {
            Intent tela = new Intent(this, Cadastre_se.class);
            startActivity(tela);
        }
    }
}
