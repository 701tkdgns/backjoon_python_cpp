import heapq, sys


def dijkstra(start):
    hq = []
    dp = [INF] * (N + 1)
    dp[start] = 0
    heapq.heappush(hq, [start, 0])
    while hq:
        route, cost = heapq.heappop(hq)
        if dp[route] < cost:
            continue
        for new_route, new_cost in lst[route]:
            best_cost = cost + new_cost
            if dp[new_route] > best_cost:
                dp[new_route] = best_cost
                heapq.heappush(hq, [new_route, best_cost])
    return dp


std = sys.stdin
N, E = map(int, std.readline().split())
INF = sys.maxsize

lst = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, std.readline().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
v1, v2 = map(int, std.readline().split())
tmp = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
res = min(tmp[v1] + v1_[v2] + v2_[N], tmp[v2] + v2_[v1] + v1_[N])
print(res if res < INF else -1)