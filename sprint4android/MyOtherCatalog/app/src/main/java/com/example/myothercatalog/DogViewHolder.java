package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class DogViewHolder extends RecyclerView.ViewHolder {
    private final TextView titulo;
    private final ImageView foto;
    private final View holder;
    //public static Button details;
    public Context context=this.itemView.getContext();

    public DogViewHolder(@NonNull View itemView){
        super(itemView);
        titulo = (TextView) itemView.findViewById(R.id.dog_name_text_view);
        foto = (ImageView) itemView.findViewById(R.id.dog_image_view);
        holder = (View) itemView.findViewById(R.id.holder);
    }

    public void showData(DogData data, Activity activity){
        titulo.setText(data.getName());
        cancelPreviousImageDownloadIfAny();
        loadImage(data.getImageUrl(), activity);
        //Bitmap image = getBitmapFromURL(data.getImageUrl());
        holder.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) { //Según la celda pulsada, se envia a DetailActivity la información necesaria en un Intent
                //Toast.makeText(context, "HOLA",Toast.LENGTH_SHORT).show();
                Intent myIntent = new Intent(context, DetailActivity.class);
                myIntent.putExtra("titulo", data.getName());
                myIntent.putExtra("foto", data.getImageUrl());
                //myIntent.putExtra("BitmapImage", image);
                context.startActivity(myIntent);
            }
        });
    }

    private void cancelPreviousImageDownloadIfAny(){}

    private void loadImage(String imageUrl, Activity activity){ //Cargamos la imagen desde el Bitmap enviado por getBitmapFromUrl
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                Bitmap image = getBitmapFromURL(imageUrl);
                activity.runOnUiThread(new Runnable(){
                    @Override
                    public void run(){
                        foto.setImageBitmap(image);
                    }
                });
            }
        });
        thread.start();
    }

    private Bitmap getBitmapFromURL(String urlString) { //Formación del Bitmap gracias a la url enviada
        Bitmap image = null;
        try {
            URL url = new URL(urlString);
            image = BitmapFactory.decodeStream(url.openConnection().getInputStream());
        }catch(IOException e){}
        return image;
    }

}


