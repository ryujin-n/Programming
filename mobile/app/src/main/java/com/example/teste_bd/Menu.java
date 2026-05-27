package com.example.teste_bd;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;


public class Menu extends AppCompatActivity implements View.OnClickListener {
    ImageButton btMNUContatos;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);


        btMNUContatos = findViewById(R.id.btMNUContatos);
        btMNUContatos.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.btMNUContatos) {
            Intent telaContatos = new Intent(this, MainActivity.class);
            startActivity(telaContatos);
        }
    }
}

