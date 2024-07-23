import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bags = []
for _ in range(N):
    v, c, k = map(int, input().split())
    while k > 0:
        bags.append([v, c])
        k -= 1
dp = [[0 for _ in range(M + 1)] for _ in range(len(bags) + 1)]
for i in range(1, len(bags) + 1):
    v, c = bags[i - 1][0], bags[i - 1][1]
    for m in range(1, M + 1):
        if v <= m:
            dp[i][m] = max(dp[i - 1][m], dp[i - 1][m - v] + c)
        else:
            dp[i][m] = dp[i - 1][m]
print(dp[len(bags)][len(dp[0]) - 1])