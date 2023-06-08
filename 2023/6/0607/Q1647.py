# import sys, heapq
#
# inf = sys.maxsize
#
#
# def dijkstra(v):
#     hq = []
#     heapq.heappush(hq, [v, 0])
#     dp[v] = 0
#     visit[v] = 1
#     while hq:
#         node, cost = heapq.heappop(hq)
#         if dp[node] < cost:
#             continue
#         for new_node, _cost in lst[node]:
#             new_cost = _cost + cost
#             if dp[new_node] > new_cost and visit[new_node] == 0:
#                 dp[new_node] = new_cost
#                 visit[new_node] = 1
#                 heapq.heappush(hq, [new_node, new_cost])
#
#
# N, M = map(int, input().split())
# lst = [[] for _ in range(N + 1)]
# visit = [0] * (N + 1)
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     lst[a].append([b, c])
#     lst[b].append([a, c])
#
# dp = [inf for _ in range(N + 1)]
# dijkstra(1)
# print(dp[1:], sum(dp[1:]))


import sys


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges, result = [], []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result.append(cost)


# https://bbbyung2.tistory.com/79