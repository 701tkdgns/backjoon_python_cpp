#include<iostream>
#include<string>
#include<stack>
using namespace std;

int solution(string s)
{
    int answer = 0;
    if (s.empty() || s.size() % 2 != 0) return answer;

    stack<char> stk;
    for (int nIndex = 0; nIndex < s.size(); nIndex++){
        if (stk.empty() || stk.top() != s[nIndex]) stk.push(s[nIndex]);
        else stk.pop();
    }
    if (stk.empty()) answer = 1;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}