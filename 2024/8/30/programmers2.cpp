#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int tri_len = triangle.size();
    vector<vector<int>> dp(tri_len, vector<int>(tri_len));
    dp[0][0] = triangle[0][0];
    for (int i = 1; i < tri_len; i++){
        for (int j = 0; j < triangle[i].size(); j++){
            if (j == 0) dp[i][j] = dp[i-1][j] + triangle[i][j];
            else dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j]);
            answer = max(answer, dp[i][j]);
        }
    }
    return answer;
}