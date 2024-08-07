import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bags = []
for _ in range(N):
    v, c, k = map(int, input().split())
    for i in range(k):
        bags.append([v, c])
bags.sort()
dp = [[0 for _ in range(M + 1)] for _ in range(len(bags) + 1)]
bags_len = len(bags)
for i in range(1, bags_len + 1):
    v, c = bags[i - 1][0], bags[i - 1][1]
    for m in range(1, M + 1):
        dp[i][m] = dp[i - 1][m]
        if v <= m:
            dp[i][m] = max(dp[i][m], dp[i - 1][m - v] + c)
print(dp[len(dp) - 1][len(dp[0]) - 1])