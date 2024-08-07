import sys
input = sys.stdin.readline
N, K = map(int, input().split())
bags = []
for _ in range(N):
    w, v = map(int, input().split())
    bags.append([w, v])
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = bags[i - 1][0], bags[i - 1][1]
    for k in range(1, K + 1):
        dp[i][k] = dp[i - 1][k]
        if w <= k:
            dp[i][k] = max(dp[i][k], dp[i - 1][k - w] + v)
print(dp[N][K])
