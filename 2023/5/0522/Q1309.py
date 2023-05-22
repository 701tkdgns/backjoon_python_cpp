n = int(input())
# dp = [[0 for _ in range(2)] for _ in range(n + 1)]
dp = [1, 3] + [0] * (n - 1)
# print(dp)
# dp[0][0], dp[1][0] = 1, 1
for i in range(2, n):
    dp[i] = dp[i - 2] + dp[i - 1] * 2
