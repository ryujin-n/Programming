package com.example.teste_bd;
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;


public class CriaBanco extends SQLiteOpenHelper {


    private static final String NOME_BANCO = "banco_exemplo.db";
    private static final int VERSAO = 2;
    public CriaBanco(Context context) {
        super(context, NOME_BANCO, null, VERSAO);
    }


    @Override
    public void onCreate(SQLiteDatabase db) {
        String sql = "CREATE TABLE contatos ("
                + "codigo integer primary key autoincrement,"
                + "nome text,"
                + "email text)";
        db.execSQL(sql);
        sql = "Create table usuarios ("
                + "codigo integer primary key autoincrement,"
                + "nome   text,"
                + "email  text,"
                + "senha  text,"
                + "cpf    text,"
                + "telefone text)";
        db.execSQL(sql);
        sql = "insert into usuarios (nome, email, senha, cpf, telefone)" +
                " values ('ADMIN', 'admin@teste.com', 'adm123', null, null)";
        db.execSQL(sql);
    }


    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS contatos");
        db.execSQL("DROP TABLE IF EXISTS usuarios");
        onCreate(db);
    }
}
