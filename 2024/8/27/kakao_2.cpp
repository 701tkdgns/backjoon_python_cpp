#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    map<string, int> dictionary;
    string w = "";
    int dictSize = 27;
    for (int i = 0; i < 26; i++){
        string ch = "";
        ch += (char)('A' + i);
        dictionary[ch] = i + 1;
    }

    for (char c : msg) {
        w += c;
        if (dictionary.find(w) == dictionary.end()) {
            string wc = w.substr(0, w.size() - 1);
            answer.push_back(dictionary[wc]);
            dictionary[w] = dictSize;
            dictSize += 1;
            w = c;
        }
    }

    if (!w.empty()) {
        answer.push_back(dictionary[w]);
    }

    return answer;
}