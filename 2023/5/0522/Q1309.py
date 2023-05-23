# N = int(input())
# dp = [0 for _ in range(N + 1)]
# dp[0], dp[1] = 1, 3
# for i in range(2, N + 1):
#     dp[i] = dp[i - 2] + dp[i - 1] * 2
# print(dp[N])
#

N = int(input())
mod = 9901
dp = [[0 for _ in range(3)] for _ in range(N + 1)]
dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1
for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod
res = (dp[N][0] + dp[N][1] + dp[N][2]) % mod
print(res)