import heapq
import sys
inf = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    while hq:
        node, wei = heapq.heappop(hq)
        if dp[node] < wei:
            continue
        for new_node, tmp_wei in lst[node]:
            new_wei = tmp_wei + wei
            if dp[new_node] == inf:
                dp[new_node] = new_wei
                heapq.heappush(hq, [new_node, new_wei])

            elif dp[new_node] > new_wei:
                dp[new_node] = new_wei
                heapq.heappush(hq, [new_node, new_wei])


n, m, k = map(int, input().split())
lst = [[] for _ in range(n + 1)]
dp = [[inf for _ in range(k)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
dijkstra(1)
for i in range(1, n + 1):
    if dp[i] == inf:
        print(-1)
    else:
        print(dp[i])