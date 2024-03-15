//
// Created by mosta on 3/15/2024.
//
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

float calc(const string& ex){
    stringstream ss(ex);
    float num1, num2, result;
    char op;
    ss >> num1;
    while(ss >> op >> num2){
        if(op == '/')
            result = num1 / num2;
        else if(op == '*')
            result = num1 * num2;
        else if(op == '+')
            result = num1 + num2;
        else if(op == '-')
            result = num1 - num2;
        num1 = result;
    }
    return result;
}

int main() {
    cout << "Welcome to our fraction calculator program!!\n\n";
    string Math_cal;
    cout << "Enter a mathematical expression: ";
    getline(cin, Math_cal);
    float result = calc(Math_cal);
    cout << "The result is: " << result << endl;
    return 0;
}
