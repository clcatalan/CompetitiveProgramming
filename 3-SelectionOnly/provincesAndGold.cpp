//https://open.kattis.com/problems/provincesandgold
#include<iostream>

using namespace std;

int main() {
    int g,s,c;
    cin >> g >> s >> c;
    
    string v = "", t;
    
    int bPow = (3*g) + (2*s) + (1*c);
    
    //determine Victory cards
    if(bPow >= 8) {
        v = "Province";
    } else if(bPow >= 5 && bPow < 8) {
        v = "Duchy";
    } else if(bPow >= 2 && bPow < 5) {
        v = "Estate";
    }
    
    //determine treasure cards
    if(bPow >= 6) {
        t = "Gold";
    } else if(bPow >= 3 && bPow < 6) {
        t = "Silver";
    } else if(bPow >= 0 && bPow < 3) {
        t = "Copper";
    }
    
    if(v != "") {
        cout << v << " or " << t << endl;
    } else {
        cout << t << endl;
    }
    
 
    return 0;
}