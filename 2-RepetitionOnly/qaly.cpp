#include<iostream>

using namespace std;

int main() {
    
    int N;
    cin >> N;
    float sum = 0;
    for(int i=0;i<N;i++) {
        float q, y;
        
        cin >> q >> y;
        
        sum += (q*y);
    }
    
    cout << sum << endl;
    return 0;
}