N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
res = -10001

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = lst[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        for x in range(i, N + 1):
            for y in range(j, M + 1):
                res = max(res, dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1])

print(res)