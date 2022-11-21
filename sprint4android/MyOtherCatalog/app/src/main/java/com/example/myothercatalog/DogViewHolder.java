package com.example.myothercatalog;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class DogViewHolder extends RecyclerView.ViewHolder {
    private final TextView titulo;
    private final ImageView foto;

    public DogViewHolder(@NonNull View itemView){
        super(itemView);
        titulo = (TextView) itemView.findViewById(R.id.dog_name_text_view);
        foto = (ImageView) itemView.findViewById(R.id.dog_image_view);
    }

    public void showData(DogData data, Activity activity){
        titulo.setText(data.getName());
        cancelPreviousImageDownloadIfAny();
        loadImage(data.getImageUrl(), activity);
    }

    private void cancelPreviousImageDownloadIfAny(){}

    private void loadImage(String imageUrl, Activity activity){
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

    private Bitmap getBitmapFromURL(String urlString) {
        Bitmap image = null;
        try {
            URL url = new URL(urlString);
            image = BitmapFactory.decodeStream(url.openConnection().getInputStream());
        }catch(IOException e){}
        return image;
    }
}


