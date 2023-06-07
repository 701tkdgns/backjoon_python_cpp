import sys, heapq
inf = sys.maxsize

def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, _cost in lst[node]:
            new_cost = _cost + cost
            if dp[new_node] > new_cost:
                dp[new_node] = new_cost
                heapq.heappush(hq, [new_node, new_cost])

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
for i in range(1, N + 1):
    dp = [inf for _ in range(N + 1)]
    dijkstra(i)
    print(dp)