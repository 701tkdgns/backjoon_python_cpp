N, K = map(int, input().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = map(int, input().split())
    for k in range(1, K + 1):
        if k < w:
            dp[i][k] = dp[i - 1][k]
        else:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - w] + v)
print(dp[N][K])
