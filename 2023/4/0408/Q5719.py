import heapq
import sys


def dijkstra(init_v):
    hq = []
    heapq.heappush(hq, [0, init_v])  # cost, node
    dp[init_v][0] = 0
    visit = [False for _ in range(N)]
    while hq:
        wei, node = heapq.heappop(hq)
        if visit[node]:
            continue
        visit[node] = True
        for new_node, new_wei in lst[node]:
            chk_wei = new_wei + wei
            if dp[new_node][1] > chk_wei:
                dp[new_node][1] = chk_wei
                dp[new_node].sort()
                heapq.heappush(hq, [chk_wei, new_node])


while True:
    N, M = map(int, input().split())
    lst = [[] for _ in range(N)]
    dp = [[sys.maxsize for _ in range(2)] for _ in range(N)]
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    for _ in range(M):
        u, v, p = map(int, input().split())
        lst[u].append([v, p])
    dijkstra(S)
    print(dp)


6549
2042
2096
