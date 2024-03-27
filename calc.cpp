#include <iostream>
#include <string>
#include "calc.h"
using namespace std;
int main() {
    cout << "Welcome to our fraction calculator program!!\n\n";
    string Math_cal;
    cout << "Enter a mathematical expression: ";
    getline(cin, Math_cal);
    calc(Math_cal);
    return 0;
}