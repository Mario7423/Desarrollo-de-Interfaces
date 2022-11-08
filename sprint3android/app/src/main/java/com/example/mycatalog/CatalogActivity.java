package com.example.mycatalog;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

public class CatalogActivity extends AppCompatActivity {
    private Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button detailButton = findViewById(R.id.detailButton);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar((Toolbar) findViewById(R.id.toolbar));
        DrawerLayout drawerLayout = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(this);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();
        detailButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(context, DetailActivity.class);
                context.startActivity(myIntent);
            }
        });
        @Override
        public void onBackPressed() {
            if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
                drawerLayout.closeDrawer(GravityCompat.START);
            } else {
                super.onBackPressed();
            }
        }
        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
            int title;
            switch (menuItem.getItemId()) {
                case R.id.nav_camera:
                    title = R.string.menu_camera;
                    break;
                case R.id.nav_gallery:
                    title = R.string.menu_gallery;
                    break;
                case R.id.nav_manage:
                    title = R.string.menu_tools;
                    break;
                case R.id.nav_share:
                    title = R.string.menu_share;
                    break;
                case R.id.nav_send:
                    title = R.string.menu_send;
                    break;
                default:
                    throw new IllegalArgumentException("menu option not implemented!!");
            }

            Fragment fragment = HomeContentFragment.newInstance(getString(title));
            getSupportFragmentManager()
                    .beginTransaction()
                    .setCustomAnimations(R.anim.nav_enter, R.anim.nav_exit)
                    .replace(R.id.home_content, fragment)
                    .commit();


            setTitle(getString(title));

            drawerLayout.closeDrawer(GravityCompat.START);

            return true;
        }

    }

}