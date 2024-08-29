#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int find_max(vector<int> land, int idx){
    int ret = 0;
    for (int i = 0; i < land.size(); i++){
        if (i != idx) ret = max(land[i], ret);
    }
    return ret;
}

int solution(vector<vector<int> > land)
{
    int answer = 0;
    int rows = land.size();
    for (int i = 1; i < rows; i++){
        for (int j = 0; j < 4; j++){
            int mx = find_max(land[i-1], j);
            land[i][j] = land[i][j] + mx;
        }
    }
    for(int i = 0; i < 4; i++){
        answer = max(answer, land[rows-1][i]);
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}