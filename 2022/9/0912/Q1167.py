import sys

input = sys.stdin.readline


def tree(node, cost):
    for i in lst[node]:
        tmp_node, tmp_cost = i
        if dp[tmp_node] == -1:
            dp[tmp_node] = cost + tmp_cost
            tree(tmp_node, cost + tmp_cost)


V = int(input())
lst = [[] for _ in range(V + 1)]
for _ in range(V):
    tmp = list(map(int, input().split()))[:-1]
    n = tmp[0]
    for i in range(1, len(tmp), 2):
        a, b = tmp[i], tmp[i + 1]
        lst[n].append([a, b])
dp = [-1 for _ in range(V + 1)]
dp[1] = 0
tree(1, 0)
mx = max(dp[1:])
idx = dp.index(mx)
dp = [-1 for _ in range(V + 1)]
dp[idx] = 0
tree(idx, 0)
res = max(dp[1:])
print(res)