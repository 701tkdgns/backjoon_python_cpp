#include <string>
#include <vector>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <unordered_map>
using namespace std;

vector<string> makeMultiset(const string &s) {
    vector<string> multiset;
    for (size_t i = 0; i < s.size() - 1; ++i) {
        if (isalpha(s[i]) && isalpha(s[i + 1])) { // 두 글자가 모두 알파벳인 경우만 추가
            string pair = "";
            pair += toupper(s[i]);
            pair += toupper(s[i + 1]);
            multiset.push_back(pair);
        }
    }
    return multiset;
}

int solution(string str1, string str2) {
    vector<string> multiset1 = makeMultiset(str1);
    vector<string> multiset2 = makeMultiset(str2);


    unordered_map<string, int> counter1, counter2;

    // multiset1의 각 쌍의 빈도를 계산
    for (const string &s : multiset1) {
        counter1[s]++;
    }

    // multiset2의 각 쌍의 빈도를 계산
    for (const string &s : multiset2) {
        counter2[s]++;
    }

    // 교집합 크기 계산
    int intersection_size = 0;
    for (const auto &pair : counter1) {
        if (counter2.find(pair.first) != counter2.end()) {
            intersection_size += min(pair.second, counter2[pair.first]);
        }
    }

    // 합집합 크기 계산
    int union_size = 0;
    for (const auto &pair : counter1) {
        union_size += pair.second;
    }
    for (const auto &pair : counter2) {
        if (counter1.find(pair.first) != counter1.end()) {
            union_size += max(0, pair.second - counter1[pair.first]);
        } else {
            union_size += pair.second;
        }
    }

    // 자카드 유사도 계산 및 결과 반환
    if (union_size == 0) {
        return 65536; // 둘 다 공집합일 경우
    } else {
        double similarity = (double)intersection_size / union_size;
        return static_cast<int>(floor(similarity * 65536));
    }
}