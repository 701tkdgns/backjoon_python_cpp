#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string modify_n(int n) {
    string v = "0";
    string conV= "0123456789ABCDEF";
    for (int i = 1; v.length() <= 100000; i++){
        int tmp = i;
        string tmp_v = "";
        while (tmp > 0) {
            tmp_v += conV[tmp % n];
            tmp = tmp / n;
        }
        reverse(tmp_v.begin(), tmp_v.end());
        v += tmp_v;
    }

    return v;
}

string solution(int n, int t, int m, int p)
{
    string answer = "";
    string v = modify_n(n);
    for(int i = p - 1; i < v.length(); i+=m) {
        answer += v[i];
        if (answer.length() == t) break;
    }

    return answer;
}