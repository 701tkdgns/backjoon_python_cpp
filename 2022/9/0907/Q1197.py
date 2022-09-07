import heapq, sys

std = sys.stdin.readline
inf = sys.maxsize


def dijkstra(x):
    hq = []
    heapq.heappush(hq, [x, 0])
    dp[x] = 0
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, tmp_cost in lst[node]:
            new_cost = tmp_cost + cost
            if dp[new_node] > new_cost:
                dp[new_node] = new_cost
                heapq.heappush(hq, [new_node, new_cost])


V, E = map(int, std().split())
lst = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, s = map(int, std().split())
    lst[a].append([b, s])
res = inf
for i in range(1, V):
    dp = [inf for _ in range(V + 1)]
    dijkstra(i)
    res = min(res, dp[V])
print(res)