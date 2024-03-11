//
// Created by mosta on 3/10/2024.
//
#include <iostream>
#include <string>
using namespace std;
int main() {
    string the_sent;
    cout << "WELCOME TO OUR ENCODING DECODING PROGRAMM !! ";
    cout << "Enter the sentence you want to encode or decode: ";
    getline(cin, the_sent);
    cout << "Enter 1 to encode and 2 to decode && the key of of the column: ";
    int choice1, choice2;
    int index1;
    int counter = 0;
    cin >> choice1 >> choice2;
    if (choice1 == 1) {
        for (int i = 0; i < the_sent.length(); i++) {
            if (isalpha(the_sent[i])) {
                counter += 1;
            }
        }
        char new_sent[counter + (choice2 - 1)];
        index1 = 0;
        for (int i = 0; i < the_sent.length(); i++) {
            if (isalpha(the_sent[i])) {
                new_sent[index1] = toupper(the_sent[i]);
                index1 += 1;
            }
        }
        while (counter % choice2 != 0) {
            new_sent[counter] = 'X';
            counter += 1;
        }
        int index2 = 0;
        int row_s = counter / choice2;
        char matrix[choice2][row_s];
        for (int rows = 0; rows < row_s; rows++) {
            for (int columns = 0; columns < choice2; columns++) {
                matrix[columns][rows] = new_sent[index2];
                index2 += 1;
            }
        }
        char matrix2[choice2][row_s];
        for (int i = 0; i < choice2; i++) {
            for (int j = 0; j < row_s; j++) {
                matrix2[i][j] = ' '; // Default value
            }
        }

        // Assign values to matrix2 only when printed from matrix
        for (int i = 0; i < (counter / choice2); i++) {
            cout << matrix[choice2 - 1][i];
            matrix2[choice2 - 1][i] = matrix[choice2 - 1][i];
        }
        for (int i = (choice2 - 2); i > 0; i--) {
            cout << matrix[i][row_s - 1];
            matrix2[i][row_s - 1] = matrix[i][row_s - 1];
        }
        for (int i = (row_s - 1); i >= 0; i--) {
            cout << matrix[0][i];
            matrix2[0][i] = matrix[0][i]; // Corrected the indices here
        }
        for (int i = 1; i < (choice2 - 1); i++) {
            cout << matrix[i][0];
            matrix2[i][0] = matrix[i][0];
        }
        int x=2;
        int y=1;
        while(true){
            if(matrix[choice2-x][y]!=matrix2[choice2-x][y]){
                cout<<matrix[choice2-x][y];
                matrix2[choice2-x][y] = matrix[choice2-x][y];
                y+=1;
            }
            else if(matrix[choice2-x-1][y-1]!=matrix2[choice2-x-1][y-1]){
                cout<<matrix[choice2-x-1][y-1];
                matrix2[choice2-x-1][y-1] = matrix[choice2-x-1][y-1];
                x+=1;
            }
            else if(matrix[choice2-x-1][y-1]!=matrix2[choice2-x-1][y-1]){
                cout<<matrix[choice2-x-1][y-1];
                matrix2[choice2-x-1][y-1] = matrix[choice2-x-1][y-1];
                y-=1;
            }
            else if(matrix[choice2-x-1+1][y-1]!=matrix2[choice2-x-1+1][y-1]){
                cout<<matrix[choice2-x-1+1][y-1];
                matrix2[choice2-x-1][y-1] = matrix[choice2-x-1][y-1];
                x-=1;
            }
            else{
                break;
            }
        }
    }
// ... (previous code remains unchanged)

    else if(choice1 == 2){
        for (int i = 0; i < the_sent.length(); i++) {
            if (isalpha(the_sent[i])) {
                counter += 1;
            }
        }
        char new_sent[counter + (choice2 - 1)];
        index1 = 0;
        for (int i = 0; i < the_sent.length(); i++) {
            if (isalpha(the_sent[i])) {
                new_sent[index1] = toupper(the_sent[i]);
                index1 += 1;
            }
        }
        int row_s = counter / choice2;
        char matrix2[choice2][row_s];
        char sps=' ';
        for (int i = 0; i < choice2; i++) {
            for (int j = 0; j < row_s; j++) {
                matrix2[i][j] = ' '; // Default value
            }
        }
        int u=0; // Initialize u to 0
        // Assign values to matrix2 only when printed from matrix
        for (int i = 0; i < (counter / choice2); i++) {
            matrix2[choice2 - 1][i] = new_sent[u];
            u+=1;
        }
        for (int i = (choice2 - 2); i > 0; i--) {
            matrix2[i][row_s - 1] = new_sent[u];
            u+=1;
        }
        for (int i = (row_s - 1); i >= 0; i--) {
            matrix2[0][i] = new_sent[u];
            u+=1;
        }
        for (int i = 1; i < (choice2 - 1); i++) {
            matrix2[i][0] = new_sent[u];
            u+=1;
        }
        int x=2;
        int y=1;
        while(u < counter){ // Check that u is less than counter
            if(char(sps) == char(matrix2[choice2-x][y])){
                matrix2[choice2-x][y] = new_sent[u];
                y+=1;
                u+=1;
            }
            else if(sps==matrix2[choice2-x-1][y-1]){
                matrix2[choice2-x-1][y-1] = new_sent[u];
                x+=1;
                u+=1;
            }
            else if(sps==matrix2[choice2-x-1][y-1]){
                matrix2[choice2-x-1][y-1] = new_sent[u];
                y-=1;
                u+=1;
            }
            else if(sps==matrix2[choice2-x-1+1][y-1]){
                matrix2[choice2-x-1][y-1] = new_sent[u];
                x-=1;
                u+=1;
            }
            else{
                break;
            }
        }
        for(int rown=0; rown< row_s;rown++){
            for(int coln=0; coln<choice2; coln++){
                cout<< matrix2[coln][rown];
            }
        }
    }


// ... (rest of the code remains unchanged)


    return 0;
}