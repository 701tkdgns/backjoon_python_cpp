#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
string AEIOU = "AEIOU";
int answer = 0;
int cnt = 0;

void dfs(string s, string word){
    if (s.length() > 5) {
        return;
    }


    if (s == word) {
        answer = cnt;
        return;
    }

    cnt ++;

    for (int i = 0; i < 5; i++){
        dfs(s + AEIOU[i], word);
    }
}

int solution(string word) {
    dfs("", word);
    return answer;
}