import heapq
import sys
std = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start, v):
    hq = []
    heapq.heappush(hq, [start, 0])
    dp = [INF for _ in range(N + 1)]
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for tmp_node, tmp_cost in lst[node]:
            if dp[tmp_node] > tmp_cost + cost:
                dp[tmp_node] = tmp_cost + cost
                heapq.heappush(hq, [tmp_node, tmp_cost + cost])
    return dp[v]


N, M, X = map(int, std().split())
lst = [[] for _ in range(N + 1)]
go = 0
for _ in range(M):
    a, b, t = map(int, std().split())
    lst[a].append([b, t])
res = 0
for i in range(1, N + 1):
    if i != X:
        res = max(dijkstra(i, X) + dijkstra(X, i), res)
print(res)





# # import sys
# #
# # sys.setrecursionlimit(10 ** 6)
# #
# #
# # def dfs(v, c):
# #     for node, time in lst[v]:
# #         if dp[node] == -1:
# #             dp[node] = c + time
# #             dfs(node, c + time)
# #
# #
# # N, M, X = map(int, input().split())
# # lst = [[] for _ in range(N + 1)]
# # go, back = 0, 0
# # for _ in range(M):
# #     a, b, t = map(int, input().split())
# #     lst[a].append([b, t])
# # dp = [-1 for _ in range(N + 1)]
# # dp[X] = 0
# # dfs(X, 0)
# # idx = dp.index(max(dp))
# # go = dp[idx]
# # print(dp)
# # dp = [-1 for _ in range(N + 1)]
# # dp[idx] = 0
# # dfs(idx, 0)
# # back = dp[X]
# # print(dp)
# # print(go + back)
