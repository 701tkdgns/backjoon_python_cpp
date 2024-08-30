#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    queue<int> q;
    for (int v : prices) q.push(v);
    int idx = 0;
    while (!q.empty()){
        int v = q.front();
        q.pop();
        int cnt = 0;
        for (int i = idx + 1; i < prices.size(); i++){
            cnt += 1;
            if (prices[i] < v) break;

        }
        answer[idx] = cnt;
        idx += 1;
    }
    return answer;
}