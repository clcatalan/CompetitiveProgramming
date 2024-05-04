#include<iostream>

using namespace std;

int N;

void printAbracadabra(int i) {
    if(i > N) {
        return;
    } else {

        cout << i << " Abracadabra" << endl;
        printAbracadabra(i+1);
    }
    
}

int main() {
    cin >> N;
    
    printAbracadabra(1);
    
    return 0;
}