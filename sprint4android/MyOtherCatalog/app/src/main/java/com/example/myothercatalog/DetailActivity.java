package com.example.myothercatalog;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.squareup.picasso.Picasso;

import java.io.IOException;
import java.net.URL;

import de.hdodenhof.circleimageview.CircleImageView;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

        String titulotet = getIntent().getStringExtra("titulo"); //Cargamos los datos enviados por el ViewHolder, además de las descripciones para cada celda
        String fotoUrl = getIntent().getStringExtra("foto");
        String desc1 = "Un perro guapo";
        String desc2 = "Un perro chulo";
        String desc3 = "Un perro mono";
        String desc4 = "Un perro pequeño";
        String desc5 = "Un perro fiel";


        TextView titulo = (TextView)findViewById(R.id.titulo);          //Cargamos los Textview y el CircleImageView para modificarlos
        ImageView foton = (CircleImageView)findViewById(R.id.camiseta);
        TextView descripcion = (TextView)findViewById(R.id.descripcion);

        Picasso.get()               //Usamos la librería Picasso para cargar las imágenes desde una url
                .load(fotoUrl)
                .into(foton);

        switch (titulotet){     //Según el título, enviamos una descripción u otra
            case "Corgi":
                descripcion.setText(desc1);
                break;
            case "Ovejero":
                descripcion.setText(desc2);
                break;
            case "Pastor Alemán":
                descripcion.setText(desc3);
                break;
            case "Pug":
                descripcion.setText(desc4);
                break;
            default:
                descripcion.setText(desc5);
                break;
        }

        titulo.setText(titulotet); //Cambiamos el titulo del TextView
    }

}
