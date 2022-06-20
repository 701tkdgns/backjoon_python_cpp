# import sys
# import heapq
#
# std = sys.stdin
# n = int(std.readline())
# m = int(std.readline())
# inf = 10 ** 10
# s = [[] for _ in range(n + 1)]
# dp = [inf for _ in range(n + 1)]
# for i in range(m):
#     a, b, w = map(int, std.readline().split())
#     s[a].append([b, w])
# start, end = map(int, std.readline().split())
#
#
# def dijkstra(start):
#     dp[start] = 0
#     hq = []
#     heapq.heappush(hq, [0, start])
#     while hq:
#         w, n = heapq.heappop(hq)
#         if dp[n] < w:
#             continue
#         for n_n, wei in s[n]:
#             n_w = w + wei
#             if dp[n_n] > n_w:
#                 dp[n_n] = n_w
#                 heapq.heappush(hq, [n_w, n_n])
#
#
# dijkstra(start)
# print(dp[end])
