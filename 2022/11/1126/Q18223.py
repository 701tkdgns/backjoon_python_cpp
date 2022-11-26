import heapq, sys
INF = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp[v] = 0
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, new_cost in lst[node]:
            best_cost = new_cost + cost
            if dp[new_node] >= best_cost:
                dp[new_node] = best_cost
                heapq.heappush(hq, [new_node, best_cost])


V, E, P = map(int, input().split())  # 1 시작, V 도착
lst = [[] for _ in range(V + 1)]
dp = [INF for _ in range(V + 1)]
direct, friend = 0, 0
for _ in range(E):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
dijkstra(1)
direct += dp[V]
friend += dp[P]
dp = [INF for _ in range(V + 1)]
dijkstra(P)
friend += dp[V]
if direct == friend:
    print("SAVE HIM")
else:
    print("GOOD BYE")