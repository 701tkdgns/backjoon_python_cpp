T = int(input())
for _ in range(T):
    N = int(input())
    coins = sorted(list(map(int, input().split())))
    M = int(input())
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = 1
    for n in range(1, N + 1):
        c = coins[n - 1]
        for m in range(1, M + 1):
            dp[n][m] = dp[n - 1][m]
            if c <= m:
                dp[n][m] = dp[n][m] + dp[n][m - c]
    # for d in dp:
    #     print(*d)
    print(dp[N][M])



# T = int(input())
# for _ in range(T):
#     N = int(input())
#     coins = sorted(list(map(int, input().split())), reverse=True)
#     M = int(input())
#     res = 0
#     dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
#     for i in range(1, N + 1):
#         dp[i][0] = 1
#     for n in range(1, N + 1):
#         for m in range(1, M + 1):
#             dp[n][m] = dp[n - 1][m]
#             if m - coins[n - 1] >= 0:
#                 dp[n][m] = dp[n][m] + dp[n][m - coins[n - 1]]
#     print(dp[N][M])