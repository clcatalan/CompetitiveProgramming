#include<iostream>

using namespace std;

int main() {
    int X, N;
    cin >> X >> N;
    
    int mSum = 0;
    for(int i=0;i<N;i++) {
        int m;
        cin >> m;
        mSum += m;
    }
    
    cout << ((X*N)-mSum) + X << endl;
    
    return 0;
}