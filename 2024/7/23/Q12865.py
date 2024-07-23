N, K = map(int, input().split())
bags = []
for _ in range(N):
    m, v = map(int, input().split())
    bags.append([m, v])
bags.sort()
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    m, v = bags[i-1][0], bags[i-1][1]
    for k in range(1, K + 1):
        if m <= k:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-m] + v)
        else:
            dp[i][k] = dp[i-1][k]
print(dp[N][K])