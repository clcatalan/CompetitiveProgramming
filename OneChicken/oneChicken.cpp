//https://open.kattis.com/problems/onechicken
#include<iostream>
#include<cmath>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    string pcs = (abs(m-n) == 1) ? " piece " : " pieces ";
    
    if(n <= m) {
        cout << "Dr. Chaz will have " << m-n << pcs << "of chicken left over!";
    } else {
        cout << "Dr. Chaz needs " << n-m << " more" << pcs << "of chicken!";
    }
    
    return 0;
}