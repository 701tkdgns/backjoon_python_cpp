# n = int(input())
# squares = []
# for i in range(1, n + 1):
#     if i * i <= n:
#         squares.append(i * i)
# dp = [1000 * 1000 + 1 for _ in range(n + 1)]
# dp[0], dp[1] = 0, 1
# for i in range(2, n + 1):
#     for s in squares:
#         if i - s < 0:
#             break
#         dp[i] = min(dp[i], dp[i - s] + 1)
# # dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# # for i in range(1, len(squares) + 1):
# #     s = squares[i - 1]
# #     for v in range(s, n + 1, s):
# #         if s <= n:
# #             dp[s][v] = dp[s][v - s] + 1
# # for d in dp:
# #     if d[-1] > 0 and d[-1] < res:
# #         res = d[-1]
# # for d in dp:
# #     print(*d)
