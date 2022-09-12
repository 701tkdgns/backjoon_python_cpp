import sys, heapq

inf = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp[v] = 0
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, tmp_cost in lst[node]:
            new_cost = tmp_cost + cost
            if dp[new_node] > new_cost:
                dp[new_node] = new_cost
                line[new_node] = node
                heapq.heappush(hq, [new_node, new_cost])


input = sys.stdin.readline
N = int(input())
M = int(input())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, s = map(int, input().split())
    lst[a].append([b, s])
start, end = map(int, input().split())
dp = [inf for _ in range(N + 1)]
line = [start for _ in range(N + 1)]
dijkstra(start)
res = []
tmp = end
while tmp != start:
    res.append(str(tmp))
    tmp = line[tmp]
res.append(str(start))
res.reverse()
print(dp[end])
print(len(res))
print(*res)
