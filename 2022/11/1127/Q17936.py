import heapq, sys

INF = sys.maxsize


def dijkstra(v):
    dp[v] = 0
    hq = []
    heapq.heappush(hq, [v, 0])
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue

        for new_node, new_cost in lst[node]:
            best_cost = new_cost + cost
            if dp[new_node] > best_cost and (see[new_node] == 0 or new_node == n - 1):
                dp[new_node] = best_cost
                heapq.heappush(hq, [new_node, best_cost])


n, m = map(int, input().split())
see = list(map(int, input().split()))
lst = [[] for _ in range(n)]
dp = [INF for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    lst[a].append([b, d])
    lst[b].append([a, d])
dijkstra(0)
print(-1 if dp[n-1] == INF else dp[n-1])
