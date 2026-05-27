package com.example.teste_bd;
import androidx.appcompat.app.AppCompatActivity;


import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


public class Cadastre_se extends AppCompatActivity implements View.OnClickListener {
    Button btCadSalvar;
    EditText txtCadNome, txtCadEmail, txtCadCPF;
    EditText txtCadSenha, txtCadConfSenha, txtCadTelefone;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cadastre_se);


        btCadSalvar = findViewById(R.id.btCadSalvar);
        txtCadNome  = findViewById(R.id.txtCadNome);
        txtCadEmail = findViewById(R.id.txtCadEmail);
        txtCadCPF   = findViewById(R.id.txtCadCPF);
        txtCadSenha = findViewById(R.id.txtCadSenha);
        txtCadTelefone = findViewById(R.id.txtCadTelefone);
        txtCadConfSenha = findViewById(R.id.txtCadConfSenha);
        btCadSalvar.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {
        if (ValidaDados()) {
            // gravar os dados
            BancoControllerUsuarios bd = new BancoControllerUsuarios(getBaseContext());
            String resultado;


            resultado = bd.insereDados(txtCadNome.getText().toString(),
                    txtCadCPF.getText().toString(),
                    txtCadTelefone.getText().toString(),
                    txtCadEmail.getText().toString(),
                    txtCadSenha.getText().toString());
            Toast.makeText(getApplicationContext(), resultado,
                    Toast.LENGTH_LONG).show();


        }else{
            // mandar mensagem de erro ao gravar os dados
            Toast.makeText(getApplicationContext(), "Erro ao gravar os dadps!",
                    Toast.LENGTH_LONG).show();
        }
    }


    public boolean ValidaDados() {
        if (txtCadNome.getText().length()==0) {
            Toast.makeText(getApplicationContext(), "O Campo Nome deve ser preenchido!",
                    Toast.LENGTH_LONG).show();
            return false;
        }
        if (txtCadCPF.getText().length()==0) {
            Toast.makeText(getApplicationContext(), "O Campo CPF deve ser preenchido!",
                    Toast.LENGTH_LONG).show();
            return false;
        }
        if (txtCadTelefone.getText().length()==0) {
            Toast.makeText(getApplicationContext(), "O Campo Telefone deve ser preenchido!",
                    Toast.LENGTH_LONG).show();
            return false;
        }
        if (txtCadEmail.getText().length()==0) {
            Toast.makeText(getApplicationContext(), "O Campo E-mail deve ser preenchido!",
                    Toast.LENGTH_LONG).show();
            return false;
        }
        if (txtCadSenha.getText().length()==0) {
            Toast.makeText(getApplicationContext(), "O Campo Senha deve ser preenchido!",
                    Toast.LENGTH_LONG).show();
            return false;
        }
        if (txtCadConfSenha.getText().length()==0) {
            Toast.makeText(getApplicationContext(), "O Campo Confirma Senha deve ser preenchido!",
                    Toast.LENGTH_LONG).show();
            return false;
        }
        if (!txtCadSenha.getText().toString().equals(txtCadConfSenha.getText().toString())) {
            Toast.makeText(getApplicationContext(), "As senhas digitadas não estão iguais!",
                    Toast.LENGTH_LONG).show();
            return false;
        }
        return true;
    }
}
