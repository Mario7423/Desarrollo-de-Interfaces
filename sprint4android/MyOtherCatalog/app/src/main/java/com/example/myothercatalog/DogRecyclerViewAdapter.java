package com.example.myothercatalog;

import android.app.Activity;
import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class DogRecyclerViewAdapter  extends RecyclerView.Adapter<DogViewHolder> {

    private List<DogData> allTheData;
    private Activity activity;

    public DogRecyclerViewAdapter(List<DogData> dataSet, Activity activity){
        this.allTheData = dataSet;
        this.activity = activity;
    }

    public DogViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType){
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.dog_view_holder, parent, false);
        return new DogViewHolder(view);
    }

    public void onBindViewHolder(DogViewHolder holder, int position){
        DogData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    public int getItemCount(){
        return allTheData.size();
    }
}
