import sys, heapq


def dijkstra(x):
    dp[x] = 0
    hq = []
    heapq.heappush(hq, (0, x))
    while hq:
        cost, node = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node in lst[node]:
            if dp[new_node] > cost + 1:
                dp[new_node] = cost + 1
                heapq.heappush(hq, (cost + 1, new_node))


MAX = int(1e9)
a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    lst[x].append(y)
    lst[y].append(x)
dp = [MAX] * (n + 1)
dijkstra(a)
if dp[b] == MAX:
    print(-1)
else:
    print(dp[b])