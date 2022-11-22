package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);
        String titulo = getIntent().getStringExtra("titulo");
        String foto = getIntent().getStringExtra("foto");
    }
}
