import heapq, sys

INF = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp = [INF for _ in range(N + 1)]
    dp[v] = 0
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue

        for new_node, new_cost in lst[node]:
            best_cost = cost + new_cost
            if dp[new_node] > best_cost:
                dp[new_node] = best_cost
                heapq.heappush(hq, [new_node, best_cost])
    return dp[1:]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N + 1)]
    visit = [False for _ in range(N + 1)]
    res, tmp = [INF for _ in range(N)], []
    for _ in range(M):
        a, b, c = map(int, input().split())
        lst[a].append([b, c])
        lst[b].append([a, c])
    K = int(input())
    friends = list(map(int, input().split()))
    for i in range(K):
        tmp.append(dijkstra(friends[i]))

    for i in range(len(tmp[i])):
        t = 0
        for j in range(K):
            t += tmp[j][i]
        res[i] = t

    res_idx = 0
    res_val = INF
    for i in range(len(res)):
        if res_val > res[i]:
            res_idx = i
            res_val = res[i]
    print(res_idx + 1)