//https://open.kattis.com/problems/quadrant
#include<iostream>

using namespace std;

int main() {
    int x, y;
    cin >> x >> y;
    
    int q;
    
    if(x > 0 && y > 0) {
        cout << 1 << endl;
    } else if(x > 0 && y < 0) {
        cout << 4 << endl;
    } else if(x < 0 && y < 0) {
        cout << 3 << endl;
    } else if(x < 0 && y > 0) {
        cout << 2 << endl;
    }
    
    return 0;
}