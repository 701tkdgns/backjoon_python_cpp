#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

vector<pair<int, int>> graph;
vector<int> stk;
int maxL, maxH, maxIdx;

int main(){
    int n;
    int L = 0, R = 0, res = 0;
    cin >> n;
    for (int i = 0; i < n; i++){
        int l, h;
        cin >> l >> h;
        graph.push_back({l, h});
        maxL = maxL < l ? l : maxL;
        maxH = maxH < h ? h : maxH;
        maxIdx = maxH == h ? l : maxIdx;
    }
    stk.resize(maxL + 1);
    for (auto & g : graph){
        stk[g.first] = g.second;
    }
    for (int i = 0; i <= maxIdx; i++){
        L = L < stk[i] ? stk[i] : L;
        res += L;
    }
    
    for (int i = maxL; i > maxIdx; i--){
        R = R < stk[i] ? stk[i] : R;
        res += R;
    }
    cout << res << endl;

    return 0;
}