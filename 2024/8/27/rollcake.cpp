#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    set<int> L;
    set<int> R;

    for (int t : topping) {
        R.insert(t);
    }

    for(int i = 0 ; i < topping.size(); i ++) {
        L.insert(topping[i]);
        bool exist = false;
        // for(int j = i + 1; j < topping.size(); j++){
        //     if (topping[j] == topping[i]) {
        //         exist = true;
        //         break;
        //     }
        // }
        if (find(topping.begin() + i + 1, topping.end(), topping[i]) != topping.end()) {exist = true;}
        if (!exist) R.erase(topping[i]);
        if (L.size() == R.size()) answer += 1;
    }
    return answer;
}