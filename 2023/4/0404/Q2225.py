N, K = map(int, input().split())
MOD = 1000000000
dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
dp[0][0] = 1
for i in range(1, K + 1):
    for j in range(N + 1):
        for m in range(j + 1):
            dp[i][j] = (dp[i][j] + dp[i-1][j-m]) % MOD

            # print("i:{} j:{} value:{}".format(i, j, dp[i]))


print(dp[K][N])








# N, K = map(int, input().split())
# MOD = 1000000000
# dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
# dp[0][0] = 1
# for i in range(1, K + 1):
#     for j in range(N + 1):
#         for m in range(j + 1):
#             dp[i][j] = (dp[i][j] + dp[i-1][j-m]) % MOD
#
#
# # https://hongjw1938.tistory.com/63