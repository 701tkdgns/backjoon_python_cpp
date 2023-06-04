f = input()
s = input()
dp = [['' for _ in range(len(f))] for _ in range(len(s))]
for i in range(len(f)):
    for j in range(len(s)):
        if f[i] == s[j]:
            dp[i][j] = dp[i - 1][j - 1] + f[i]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(len(dp[len(f) - 1][len(s) - 1]))
print(dp[len(f) - 1][len(s) - 1])
