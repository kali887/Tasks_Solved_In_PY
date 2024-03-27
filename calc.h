//
// Created by mosta on 3/27/2024.
//

#ifndef MY_PROJECTS_AND_TASKS_CALC_H
#define MY_PROJECTS_AND_TASKS_CALC_H
#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}
void calc(string& ex) {
    stringstream ss(ex);
    int num1, num2, num3, num4;
    char op, op2, op3;
    ss >> num1 >> op >> num2;
    if (ss >> op2 >> num3) {
        if (ss >> op3 >> num4) {
            if(op == '*' ){
                num1*=num2;
                num2=1;
                op='/';
            }
            if(op == '+'){
                num1+=num2;
                num2=1;
                op='/';
            }
            if(op == '-'){
                num1-=num2;
                num2=1;
                op='/';
            }
            if(op3 == '*' ){
                num3*=num4;
                num4=1;
                op3='/';
            }
            if(op3 == '+'){
                num3+=num4;
                num4=1;
                op3='/';
            }
            if(op3 == '-'){
                num3-=num4;
                num4=1;
                op3='/';

            }
            if(op == '/' && op2 == '/' && op3 == '/'){
                num1 *= num4;
                num2 *= num3;
                cout << num1/gcd(num1, num2) << "/" << num2/gcd(num1, num2);
            }
            if((op2 == '+' || op2 == '-') && op == '/' && op3 == '/'){
                if(op2 == '+' ){
                    num1 = (num1 * num4) + (num2 * num3);
                }
                else{
                    num1 = (num1 * num4) - (num2 * num3);
                }                num2 *= num4;
                cout << num1/gcd(num1, num2) << "/" << num2/gcd(num1, num2);
            }
            if(op2 == '*')
            {
                num1*=num3;
                num2*=num4;
                cout<<num1/gcd(num1, num2)<<op<<num2/gcd(num1, num2);
            }
        }
        else {
            if(op == '/' && op2 == '/')
                cout<<"invalid Expresstion ";
            if(op == '*' ){
                num1*=num2;
                num2=1;
                num4=1;
                op3='/';
                op='/';
            }
            if(op == '+'){
                num1+=num2;
                num2=1;
                num4=1;
                op3='/';
                op='/';
            }
            if(op == '/'){
                num4=1;
                op3='/';
            }
            if(op == '-'){
                num1-=num2;
                num2=1;
                num4=1;
                op3='/';
                op='/';
            }
            if(op == '/' && op2 == '/' && op3 == '/'){
                num1 *= num4;
                num2 *= num3;
                cout << num1/gcd(num1, num2) << "/" << num2/gcd(num1, num2);
            }
            if((op2 == '+' || op2 == '-') && op == '/' && op3 == '/'){
                if(op2 == '+' ){
                    num1 = (num1 * num4) + (num2 * num3);
                }
                else{
                    num1 = (num1 * num4) - (num2 * num3);
                }
                num2 *= num4;
                cout << num1/gcd(num1, num2) << "/" << num2/gcd(num1, num2);
            }
            if(op2 == '*')
            {
                num1*=num3;
                num2*=num4;
                cout<<num1/gcd(num1, num2)<<op<<num2/gcd(num1, num2);
            }
        }
    }
    else {
        if(op == '/')
            cout<<num1/gcd(num1, num2)<<op<<num2/gcd(num1, num2);
        else if(op == '*')
            cout<< num1 * num2;
        else if(op == '+')
            cout<<num1 + num2;
        else if(op == '-')
            cout<<num1 - num2;
    }
}
#endif //MY_PROJECTS_AND_TASKS_CALC_H
