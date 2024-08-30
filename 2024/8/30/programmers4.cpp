#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    for (const string& skill_tree : skill_trees){
        int idx = 0;
        for (const char& sk : skill_tree){
            if (find(skill.begin(), skill.end(), sk) != skill.end()){
                if (skill[idx] == sk){
                    idx += 1;
                } else {
                    idx = -1;
                    break;
                }
            }
        }
        if (idx != -1) answer += 1;
    }
    return answer;
}