
# T = int(input())
# for _ in range(T):
#     K = int(input())
#     lst = list(map(int, input().split()))
#     dp = [[0 for _ in range(K)] for _ in range(K)]
#     for i in range(K - 1):
#         dp[i][i + 1] = lst[i] + lst[i + 1]
#         for j in range(i + 2, K):
#             dp[i][j] = dp[i][j-1] + lst[j]
#
#     for d in range(2, K):
#         for i in range(K - d):
#             j = i + d
#             _min = [dp[i][K] + dp[K+1][j] for _ in range(i, j)]
#             dp[i][j] += min(_min)
#
#     for i in dp:
#         print(i)
#
#     T = int(input())
#     for _ in range(T):
#         k = int(input())
#         page = list(map(int, input().split()))
#         table = [[0 for _ in range(k)] for _ in range(k)]
#         for i in range(k - 1):
#             table[i][i + 1] = page[i] + page[i + 1]
#             for j in range(i + 2, k):
#                 table[i][j] = table[i][j - 1] + page[j]
#
#         for d in range(2, k):
#             for i in range(k - d):
#                 j = i + d
#                 _min = [table[i][k] + table[k + 1][j] for _ in range(i, j)]
#                 table[i][j] += min(_min)
#         print(table[0][k - 1])
#
#     # https://suri78.tistory.com/15
