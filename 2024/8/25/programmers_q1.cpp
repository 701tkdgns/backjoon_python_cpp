#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int binary_count = 0, z_count = 0;
    while (s != "1"){
        string tmp = "";
        for (char c : s) {
            if (c == '1') tmp += c;
            else z_count += 1;
        }
        int tmp_i = tmp.size();
        tmp = "";
        while(tmp_i > 0) {
            tmp = tmp + to_string(tmp_i % 2);
            tmp_i = tmp_i / 2;
        }
        s = tmp;
        binary_count += 1;
    }
    answer = {binary_count, z_count};
    return answer;
}