package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class DogData {
    private String name;
    private String imageUrl;

    public DogData(String name, String imageUrl){
        this.name = name;
        this.imageUrl = imageUrl;
    }

    public DogData(JSONObject json){
        try{
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
        }catch (JSONException error){
            error.printStackTrace();
        }
    }

    public String getName(){
        return this.name;
    }

    public String getImageUrl(){
        return this.imageUrl;
    }
}
