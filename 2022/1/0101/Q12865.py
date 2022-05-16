# import sys
#
#
# def knapsack(n, k):
#     if n < 0:
#         return 0
#     if dp[n][k] == 0:
#         if W[n] > K:
#             dp[n][k] = knapsack(n - 1, k)
#         elif W[n] <= k:
#             dp[n][k] = max(knapsack(n - 1, k), V[n] + knapsack(n - 1, k - W[n]))
#     return dp[n][k]
#
#
# N, K = map(int, sys.stdin.readline().split())
# W, V = [], []
# dp = [[0] * (K + 1) for row in range(N)]
# for _ in range(N):
#     w, v = map(int, sys.stdin.readline().split())
#     W.append(w)
#     V.append(v)
# print(knapsack(N - 1, K))