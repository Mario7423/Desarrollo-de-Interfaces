package com.example.myothercatalog;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Context context = this;
        //Button details = DogViewHolder.details;

        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/Mario7423/Desarrollo-de-Interfaces/main/API-REST/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        List<DogData> dogs = new ArrayList<>();
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                JSONObject dog = response.getJSONObject(i);
                                DogData data = new DogData(dog);
                                dogs.add(data);
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }
                        DogRecyclerViewAdapter adapter = new DogRecyclerViewAdapter(dogs, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(activity, "ERROR", Toast.LENGTH_SHORT).show();
                    }
                });
       /* DogViewHolder.details.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(context, DetailActivity.class);
                context.startActivity(myIntent);
            }
        });*/
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }
}
