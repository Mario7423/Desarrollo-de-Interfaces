package com.example.calculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView screen;
    private Button ac, power, back, div, mul, one, two, three, four, five, six, seven, eight, nine, zero, ans, add, point, equal;
    private String input, answer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        screen=findViewById(R.id.pantalla);
        ac=findViewById(R.id.ac);
        power=findViewById(R.id.power);
        back=findViewById(R.id.back);
        div=findViewById(R.id.div);
        mul=findViewById(R.id.mul);
        one=findViewById(R.id.one);
        two=findViewById(R.id.two);
        three=findViewById(R.id.three);
        four=findViewById(R.id.four);
        five=findViewById(R.id.five);
        six=findViewById(R.id.six);
        seven=findViewById(R.id.seven);
        eight=findViewById(R.id.eight);
        nine=findViewById(R.id.nine);
        zero=findViewById(R.id.zero);
        add=findViewById(R.id.plus);
        ans=findViewById(R.id.ans);
        equal=findViewById(R.id.equal);
        point=findViewById(R.id.point);
    }
    public void ButtonClick(View view){
        Button button=(Button) view;
        String data=button.getText().toString();

        switch (data){
            case "AC":
                input="";
                break;
            case "ans":
                input+=answer;
                break;
            case "x":
                solve();
                input+="*";
                break;
            case "^":
                solve();
                input+="^";
                break;
            case "=":
                solve();
                answer=input;
                break;
            case "--":
                String newText=input.substring(0,input.length()-1);
                input=newText;
                break;
            default:
                if(input==null){
                    input="";
                }
                if(data.equals("+")||data.equals("-")||data.equals("/")){
                    solve();
                }
                input+=data;


        }
        screen.setText(input);
    }

    private void solve(){
        if(input.split("\\*").length==2){
            String number[]=input.split("\\*");
            try {
                double mul = Double.parseDouble(number[0]) * Double.parseDouble(number[1]);
                input = mul+"";
            }catch(Exception e){}
        }
        else if(input.split("/").length==2){
            String number[]=input.split("/");
            try {
                double div = Double.parseDouble(number[0]) / Double.parseDouble(number[1]);
                input = div+"";
            }catch(Exception e){}
        }
        else if(input.split("\\^").length==2){
            String number[]=input.split("\\^");
            try {
                double pow = Math.pow(Double.parseDouble(number[0]), Double.parseDouble(number[1]));
                input = pow+"";
            }catch(Exception e){}
        }
        else if(input.split("\\+").length==2){
            String number[]=input.split("\\+");
            try {
                double sum = Double.parseDouble(number[0]) + Double.parseDouble(number[1]);
                input = sum+"";
            }catch(Exception e){}
        }
        else if(input.split("-").length>1){
            String number[]=input.split("-");
            if(number[0]=="" && number.length==2){
                number[0]=0+"";
            }
            try {
                double sub=0;
                if(number.length==2){
                    sub = Double.parseDouble(number[0]) - Double.parseDouble(number[1]);
                }
                else if(number.length==3){
                    sub = Double.parseDouble(number[0]) - Double.parseDouble(number[1]);
                }
                input = sub+"";
            }catch(Exception e){}
        }

        String n[]=input.split("\\.");
        if(n.length>1){
            if(n[1].equals("0")){
                input=n[0];
            }
        }
        screen.setText(input);

    }
}