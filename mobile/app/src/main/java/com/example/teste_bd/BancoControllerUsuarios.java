package com.example.teste_bd;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
public class BancoControllerUsuarios {
    private SQLiteDatabase db;
    private CriaBanco banco;


    public BancoControllerUsuarios(Context context) {
        banco = new CriaBanco(context);
    }


    public Cursor ConsultaLogin(String email, String senha) {
        Cursor cursor;
        String[] campos = { "codigo", "nome", "email", "cpf", "senha", "telefone"};
        String where = "email = '" + email + "' and senha = '" + senha + "'";
        db = banco.getReadableDatabase();
        cursor = db.query("usuarios", campos, where, null, null, null,
                null, null);
        if (cursor != null) {
            cursor.moveToFirst();
        }


        db.close();
        return cursor;
    }


    // gravar dados
    public String insereDados(String txtNome, String txtCpf, String txtTelefone,
                              String txtEmail, String txtSenha) {
        ContentValues valores;
        long resultado;
        db = banco.getWritableDatabase();


        valores = new ContentValues();
        valores.put("nome", txtNome);
        valores.put("CPF", txtCpf);
        valores.put("telefone", txtTelefone);
        valores.put("email", txtEmail);
        valores.put("senha", txtSenha);


        resultado = db.insert("usuarios", null, valores);
        db.close();


        if (resultado == -1)
            return "Erro ao inserir registro do usuário";
        else
            return "Registro Inserido com sucesso";
    }


}
