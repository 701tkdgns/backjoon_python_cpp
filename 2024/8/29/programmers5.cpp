#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map<string, int> origin_want;
    for(int i = 0; i < want.size(); i++){
        if (!origin_want[want[i]]) {
            origin_want[want[i]] = 0;
        }
        origin_want[want[i]] = number[i];
    }
    for (int i = 0; i < discount.size(); i++){
        map<string, int> cal_want = origin_want;
        if (i + 10 > discount.size()) break;

        for (int j = i; j < i + 10; j++){
            if (!cal_want[discount[j]]) break;
            else cal_want[discount[j]] -= 1;
        }

        bool chk = true;
        for (auto kv : cal_want){
            if (kv.second != 0) {
                chk = false;
                break;
            }
        }
        if (chk) answer += 1;
    }




    return answer;
}