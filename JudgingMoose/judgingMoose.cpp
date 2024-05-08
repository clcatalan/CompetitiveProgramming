//https://open.kattis.com/problems/judgingmoose
#include<iostream>

using namespace std;

int main() {
    
    int l, r;
    cin >> l >> r;
    
    if(l <= 0 && r <= 0) {
        cout << "Not a moose" << endl;
        return 0;
    }
    
    if(l == r) {
        cout << "Even " << l+r << endl;
    } else {
        cout << "Odd " << 2*max(l,r) << endl;
    }
    
    return 0;
}