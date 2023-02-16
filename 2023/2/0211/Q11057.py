n = int(input())

dp = [[0 for _ in range(10)] for _ in range(1001)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
            continue
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % con
res = 0
for i in range(10):
    res += dp[n][i]
print(res)