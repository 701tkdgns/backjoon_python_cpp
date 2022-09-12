import sys, heapq
input = sys.stdin.readline


def Prim(v):
    hq = [[v, 0]]
    dp = [False for _ in range(V + 1)]
    cnt, ans = 0, 0
    while hq:
        if cnt == V:
            break
        node, cost = heapq.heappop(hq)
        if not dp[node]:
            dp[node] = True
            ans += cost
            cnt += 1
            for new_node, new_cost in lst[node]:
                heapq.heappush(hq, [new_node, new_cost])
    return ans


V, E = map(int, input().split())
lst = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
res = Prim(1)
print(res)
