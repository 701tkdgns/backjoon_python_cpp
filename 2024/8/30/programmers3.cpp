#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    stack<int> stk;
    stack<int> boxes;
    for (int i = order.size() ; i >= 1; i--) boxes.push(i);
    while (!boxes.empty()){
        int box = boxes.top();
        boxes.pop();
        if (box != order[answer]){
            while (!stk.empty() && stk.top() == order[answer]) {
                stk.pop();
                answer += 1;
            }
            stk.push(box);
        } else {
            answer += 1;
        }
    }
    while (!stk.empty()){
        int box = stk.top();
        stk.pop();
        if (box == order[answer]) answer += 1;
        else break;
    }
    return answer;
}