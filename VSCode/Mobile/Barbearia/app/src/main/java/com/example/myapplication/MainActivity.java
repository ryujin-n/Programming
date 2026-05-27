package com.example.myapplication;

import android.content.res.ColorStateList;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.graphics.drawable.DrawableCompat;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.google.android.material.snackbar.Snackbar;


public class MainActivity extends AppCompatActivity {
    EditText nome, senha;
    Button btoLogin;
    View vLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        nome = findViewById(R.id.txtNome);
        senha = findViewById(R.id.txtSenha);
        btoLogin = findViewById(R.id.btoLogin);
        vLogin = findViewById(R.id.main);
        btoLogin.setOnClickListener(v ->{
            String txtnome = nome.getText().toString().trim();
            String txtsenha = senha.getText().toString().trim();

            if (txtnome.isEmpty() || txtsenha.isEmpty()){
                showSnackbar("Preencha todos os campos", "erro");
                return;
            }
        });
    }
    private void showSnackbar(String mensagem, String tipo) {
        Snackbar snackbar = Snackbar.make(vLogin, mensagem, Snackbar.LENGTH_SHORT);

        switch (tipo) {
            case "erro":
                applyCustomSnackbarStyle(snackbar, R.drawable.bg_snackbar_error, R.color.md_error);
                break;
            case "warning":
                applyCustomSnackbarStyle(snackbar, R.drawable.bg_snackbar_warning, R.color.md_warning);
                break;
            case "sucesso":
                applyDefaultSnackbarStyle(snackbar, R.color.md_success, R.color.md_on_success);
                break;
            default:
                applyDefaultSnackbarStyle(snackbar, R.color.md_surface_variant, R.color.md_on_surface);
                break;
        }
        snackbar.show();
    }

    private void applyCustomSnackbarStyle(Snackbar snackbar, int backgroundRes, int colorRes) {
        View snackView = snackbar.getView();
        snackView.setBackgroundResource(backgroundRes);
        snackView.setBackgroundTintList(null);

        if (snackView.getLayoutParams() instanceof ViewGroup.MarginLayoutParams) {
            ViewGroup.MarginLayoutParams params = (ViewGroup.MarginLayoutParams) snackView.getLayoutParams();
            params.setMargins(48, 0, 48, 64);
            snackView.setLayoutParams(params);
        }

        TextView tv = snackView.findViewById(com.google.android.material.R.id.snackbar_text);
        tv.setTextColor(ContextCompat.getColor(this, colorRes));
        
        Drawable infoIcon = ContextCompat.getDrawable(this, R.drawable.ic_info);
        if (infoIcon != null) {
            infoIcon = DrawableCompat.wrap(infoIcon).mutate();
            DrawableCompat.setTint(infoIcon, ContextCompat.getColor(this, colorRes));
            tv.setCompoundDrawablesWithIntrinsicBounds(infoIcon, null, null, null);
            tv.setCompoundDrawablePadding(24);
        }
    }
    private void applyDefaultSnackbarStyle(Snackbar snackbar, int bgColorRes, int textColorRes) {
        View snackView = snackbar.getView();
        snackView.setBackgroundTintList(ColorStateList.valueOf(ContextCompat.getColor(this, bgColorRes)));
        TextView tv = snackView.findViewById(com.google.android.material.R.id.snackbar_text);
        tv.setTextColor(ContextCompat.getColor(this, textColorRes));
    }
}