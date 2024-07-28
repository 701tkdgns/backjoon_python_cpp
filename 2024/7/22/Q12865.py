N, M = map(int, input().split())
bags, dp = [], [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for _ in range(N):
    m, v = map(int, input().split())
    bags.append([m, v])
bags.sort()
for i in range(1, N + 1):
    m, v = bags[i - 1][0], bags[i - 1][1]
    for k in range(1, M + 1):
        dp[i][k] = dp[i - 1][k]
        if m <= k:
            dp[i][k] = max(dp[i][k], dp[i - 1][k - m] + v)
print(dp[N][M])