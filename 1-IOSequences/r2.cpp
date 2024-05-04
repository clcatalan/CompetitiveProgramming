#include<iostream>

using namespace std;

int main() {
    int R1, S;
    cin >> R1;
    cin >> S;

    /*
        S = (R1+R2)/2;
        R2 = 2S - R1;
    */

    cout << (2*S) - R1 << endl;
    return 0;
}