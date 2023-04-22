f = input()
s = input()
t = input()

len_f, len_s, len_t = len(f), len(s), len(t)

dp = [[[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)] for _ in range(len_f + 1)]
for i in range(len(f)):
    for j in range(len(s)):
        for k in range(len(t)):
            if f[i] == s[j] == t[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(max(dp[i-1][j][k], dp[i][j-1][k]), dp[i][j][k-1])
print(dp[len_f - 1][len_s - 1][len_t - 1])