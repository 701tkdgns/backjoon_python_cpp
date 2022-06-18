# def getSmallIndex():
#     mn = INF
#     idx = 0
#     for i in range(n):
#         if d[i] < mn and not visit[i]:
#             mn = d[i]
#             idx = i
#     return idx
#
#
# def dijkstra(start):
#     for i in range(n):
#         d[i] = lst[start][i]
#     visit[start] = True
#     for i in range(n - 1):
#         current = getSmallIndex()
#         visit[current] = True
#         for j in range(n):
#             if not visit[j] and d[current] + lst[current][j] < d[j]:
#                 d[j] = d[current] + lst[current][j]
#
#
# n = 6
# INF = 10**10
# lst = [
#     [0, 2, 5, 1, INF, INF],
#     [2, 0, 3, 2, INF, INF],
#     [5, 3, 0, 3, 1, 5],
#     [1, 2, 3, 0, 1, INF],
#     [INF, INF, 1, 1, 0, 2],
#     [INF, INF, 5, INF, 2, 0],
# ]
# visit = [0 for _ in range(n)]
# d = [False for _ in range(n)]
# dijkstra(0)

################################

import heapq
