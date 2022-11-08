package com.example.mycatalog;

import android.content.Context;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class AboutActivity extends AppCompatActivity {
    private Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.about_activity);
    }
}