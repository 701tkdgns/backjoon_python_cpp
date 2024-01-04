# T = int(input())
# for _ in range(T):
#     K = int(input())
#     lst = list(map(int, input().split()))
#     dp = [[0 for _ in range(K)] for _ in range(K)]
#
#     for i in range(K - 1):
#         dp[i][i + 1] = lst[i] + lst[i + 1]
#         for j in range(i + 2, K):
#             dp[i][j] = dp[i][j - 1] + lst[j]
#
#     for d in range(2, K):
#         for i in range(K - d):
#             j = i + d
#             _min = [dp[i][K] + dp[K + 1][j] for K in range(i, j)]
#             # print(_min)
#             dp[i][j] += min(_min)
#
#     # for i in range(K):
#     #     for j in range(K):
#     #         print(dp[i][j], end=" ")
#     #     print()
#
#     print(dp[0][K - 1])
# https://suri78.tistory.com/15


T = int(input())
for _ in range(T):
    k = int(input())
    lst = list(map(int, input().split()))
    dp = [[0 for _ in range(k)] for _ in range(k)]

    for i in range(k - 1):
        dp[i][i + 1] = lst[i] + lst[i + 1]
        for j in range(i + 2, k):
            dp[i][j] = dp[i][j - 1] + lst[j]

    for d in range(2, k):
        for i in range(k - d):
            j = i + d
            _min = [dp[i][k] + dp[k + 1][j] for k in range(i, j)]
            dp[i][j] += min(_min)
