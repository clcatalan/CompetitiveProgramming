//https://open.kattis.com/problems/isithalloween
#include<iostream>
#include<string>
using namespace std;

int main() {
    string m, d;
    
    cin >> m >> d;
    
    string res = ((m == "OCT" && d == "31") || (m == "DEC" && d == "25")) ? "yup" : "nope";
    cout << res << endl;
    
    return 0;
}