F = input()
S = input()
T = input()

f, s, t = len(F), len(S), len(T)

dp = [[[0 for _ in range(t + 1)] for _ in range(s + 1)] for _ in range(f + 1)]

for i in range(1, f + 1):
    for j in range(1, s + 1):
        for k in range(1, t + 1):
            if F[i-1] == S[j - 1] == T[k - 1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i][j][k - 1], max(dp[i][j-1][k], dp[i-1][j][k]))
res = -1
for i in range(f + 1):
    for j in range(s + 1):
        for k in range(t + 1):
            res = max(res, dp[i][j][k])
print(res)