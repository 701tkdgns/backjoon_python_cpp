#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n = 0, p = 0, s = 0;
    vector<int> potatos;
    cin >> n;
    potatos.resize(n);
    for (int i = 0; i < n; i++){
        int tmp;
        cin >> tmp;
        potatos[i] = tmp;
    }
    sort(potatos.begin(), potatos.end(), greater<int>());
    if (n % 2 == 0){
        for (int i = 0; i < n / 2; i++){
            p += potatos[i];
            s += potatos[(n - 1) - i];
        }
    } else {
        for (int i = 0; i < n / 2; i++ ) {
            p += potatos[i];
            s += potatos[(n - 1) - i];
        }
        p += potatos[n / 2];
    }
    cout << s << " " << p << endl;
    return 0;
}