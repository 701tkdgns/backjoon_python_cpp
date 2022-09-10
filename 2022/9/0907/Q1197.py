import heapq, sys
std = sys.stdin.readline
inf = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
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
lst = [[] for _ in range(V)]
dp = [inf for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, std().split())
    lst[a-1].append([b-1, c])
    lst[b-1].append([a-1, c])
dijkstra(0)
print(dp[V-1])