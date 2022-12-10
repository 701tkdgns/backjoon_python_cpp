import sys, heapq

inf = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp = [inf for _ in range(A + 1)]
    p = [0 for _ in range(A + 1)]
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, tmp_cost in lst[node]:
            new_cost = cost + tmp_cost
            if dp[new_node] > new_cost:
                dp[new_node] = new_cost
                p[new_node] = node
                heapq.heappush(hq, [new_node, new_cost])
    return p


A, B = map(int, input().split())
lst = [[] for _ in range(A + 1)]
node_lst = []
for _ in range(B):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
parent = dijkstra(1)
print(A - 1)
for i in range(2, A + 1):
    print(i, parent[i])
