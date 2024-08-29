#include <string>
#include <vector>
#include <queue>
#include <sstream>
#include <unordered_map>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    priority_queue<int> max_hq;
    priority_queue<int, vector<int>, greater<int>> min_hq;
    unordered_map<int, int> count_map;
    for (int i = 0; i < operations.size(); i++){
        string s = operations[i];
        char cmd = s[0];
        int value = stoi(s.substr(2));
        if (cmd == 'I') {
            max_hq.push(value);
            min_hq.push(value);
            count_map[value]++;
        } else if (cmd == 'D'){
            if (value == 1) {
                while(!max_hq.empty() && count_map[max_hq.top()] == 0) {
                    max_hq.pop();
                }
                if (!max_hq.empty()){
                    int max_value = max_hq.top();
                    max_hq.pop();
                    count_map[max_value]--;
                }
            } else {
                while (!min_hq.empty() && count_map[min_hq.top()] == 0) {
                    min_hq.pop();
                }
                if (!min_hq.empty()) {
                    int min_value = min_hq.top();
                    min_hq.pop();
                    count_map[min_value]--;
                }
            }
        }
    }

    // Synchronize both heaps
    while (!max_hq.empty() && count_map[max_hq.top()] == 0) {
        max_hq.pop();
    }
    while (!min_hq.empty() && count_map[min_hq.top()] == 0) {
        min_hq.pop();
    }

    if (max_hq.empty() || min_hq.empty()) {
        answer = {0, 0};
    } else {
        int min_value = min_hq.top();
        int max_value = max_hq.top();
        answer = {max_value, min_value};
    }
    return answer;
}