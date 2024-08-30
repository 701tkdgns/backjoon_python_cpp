#include <string>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    // priority_queue<int, vector<int>, greater<int>> pq;
    priority_queue<int> pq;

    for (const int& work : works) pq.push(work);

    while (n > 0){
        int v = pq.top();
        pq.pop();
        if (v < 1) break;
        v -= 1;
        pq.push(v);
        n -= 1;
    }
    while (!pq.empty()){
        int v = pq.top();
        pq.pop();
        answer += pow(v, 2);
    }

    return answer;
}