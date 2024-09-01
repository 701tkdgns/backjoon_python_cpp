def solution(m, n, puddles):
    MOD = 1000000007

    # DP 테이블 초기화
    dp = [[0] * m for _ in range(n)]

    # 물에 잠긴 지역 처리
    for x, y in puddles:
        dp[y - 1][x - 1] = -1  # -1로 표시하여 물에 잠긴 지역 처리

    # 시작점 설정
    if dp[0][0] != -1:
        dp[0][0] = 1

    # DP 테이블 채우기
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            if i > 0 and dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j]
            if j > 0 and dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD

    # 결과 반환
    return dp[n - 1][m - 1]