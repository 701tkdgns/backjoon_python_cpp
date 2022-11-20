import sys, heapq

INF = sys.maxsize


def dijkstra(start):
    hq = []
    dp = [INF for _ in range(n + 1)]
    tmp = [0 for _ in range(n + 1)]
    heapq.heappush(hq, [start, 0])
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue

        for new_node, new_cost in lst[node]:
            best_cost = new_cost + cost
            if dp[new_node] > best_cost:
                dp[new_node] = best_cost
                heapq.heappush(hq, [new_node, best_cost])
                tmp[new_node] = node
    tmp[start] = '-'

    for i in range(n):
        res[i][start-1] = tmp[i + 1]


n, m = map(int, input().split())
lst = [[] for _ in range(n + 1)]
res = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    lst[a].append([b, w])
    lst[b].append([a, w])

for i in lst:
    i.sort()

for i in range(1, n + 1):
    dijkstra(i)

for i in res:
    print(*i)