import heapq
import sys

inf = sys.maxsize

def dijkstra(v):
    hq = []
    dp[v] = 0
    heapq.heappush(hq, [v, 0])
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            pass
        for new_node, new_cost in lst[node]:
            best_cost = cost + new_cost
            if dp[new_node] > best_cost:
                dp[new_node] = best_cost
                heapq.heappush(hq, [new_node, best_cost])


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
dp = [inf for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    lst[a].append([b, d])
dijkstra(1)
print(dp)
