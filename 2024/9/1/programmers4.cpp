#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    long long MOD = 1000000007;
    vector<vector<long long>> dp(n, vector<long long>(m, 0));  // 초기값을 0으로 설정

    // 물에 잠긴 지역 처리
    for (const vector<int>& puddle : puddles) {
        int x = puddle[0] - 1;
        int y = puddle[1] - 1;
        dp[y][x] = -1;  // 물에 잠긴 지역은 -1로 표시
    }

    // 시작점 설정
    dp[0][0] = (dp[0][0] != -1) ? 1 : 0;

    // DP 테이블 채우기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dp[i][j] == -1) continue;  // 물에 잠긴 지역은 무시

            // 위쪽 셀에서 오는 경우
            if (i > 0 && dp[i-1][j] != -1) {
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD;
            }

            // 왼쪽 셀에서 오는 경우
            if (j > 0 && dp[i][j-1] != -1) {
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD;
            }
        }
    }

    // 결과 반환
    return dp[n-1][m-1] % MOD;
}