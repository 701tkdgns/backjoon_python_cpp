import heapq, sys
input = sys.stdin.readline
inf = sys.maxsize


def dijkstra(i):
    hq = []
    _dp = [inf for _ in range(n + 1)]
    heapq.heappush(hq, [i, 0])
    while hq:
        node, cost = heapq.heappop(hq)
        if _dp[node] < cost:
            continue
        for new_node, new_cost in lst[node]:
            check_cost = cost + new_cost
            if _dp[new_node] > check_cost:
                _dp[new_node] = check_cost
                heapq.heappush(hq, [new_node, check_cost])
    return _dp


n, m = map(int, input().split())
lst = [[] for _ in range(n + 1)]
res = inf
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
s, t = map(int, input().split())
dp = dijkstra(s)
print(dp[t])
