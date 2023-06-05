<<<<<<< HEAD
=======
import sys

input = sys.stdin.readline
F = [""] + list(map(str, input().rstrip()))
S = [""] + list(map(str, input().rstrip()))
dp = [["" for _ in range(len(S))] for _ in range(len(F))]

for i in range(1, len(F)):
    for j in range(1, len(S)):
        if F[i] == S[j]:
            dp[i][j] = dp[i - 1][j - 1] + F[i]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
f, s = len(F), len(S)

print(len(dp[f - 1][s - 1]))
print(dp[f - 1][s - 1])
>>>>>>> 7201c018fbaab2b6ad5d8e4be1d74f3ab5321580
