#include<iostream>
#include<cmath>


using namespace std;

int main() {
    long int t, n;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n;
        long r = (sqrt(1+(8*n))-1)/2;
        cout << r << endl;
    }
   return 0;
}