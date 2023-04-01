import heapq
import sys
inf = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp[v][0] = 0
    while hq:
        node, wei = heapq.heappop(hq)
        for new_node, tmp_wei in lst[node]:
            new_wei = tmp_wei + wei
            if new_wei < dp[new_node][k - 1]:
                dp[new_node][k - 1] = new_wei
                dp[new_node].sort()
                heapq.heappush(hq, [new_node, new_wei])


n, m, k = map(int, input().split())
lst = [[] for _ in range(n + 1)]
dp = [[inf for _ in range(k)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
dijkstra(1)
for i in range(1, n + 1):
    if dp[i][k-1] == inf:
        print(-1)
    else:
        print(dp[i][k - 1])