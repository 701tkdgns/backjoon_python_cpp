#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer(numbers.size());
    stack<int> stk;
    for (int i = 0; i < numbers.size(); i++){
        while(!stk.empty() && numbers[stk.top()] < numbers[i]){
            int idx = stk.top();
            stk.pop();
            answer[idx] = numbers[i];
        }
        stk.push(i);
    }
    while (!stk.empty()){
        int idx = stk.top();
        stk.pop();
        answer[idx] = -1;
    }
    return answer;
}