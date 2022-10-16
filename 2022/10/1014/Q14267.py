import sys
sys.setrecursionlimit(10 ** 6)


def dfs(v):
    for k in node[v]:
        dp[k] += dp[v]
        dfs(k)


n, m = map(int, input().split())
employee = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
node = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    if employee[i - 1] != -1:
        node[employee[i - 1]].append(i)

for j in range(m):
    i, w = map(int, input().split())
    dp[i] += w
dfs(1)

print(*dp[1:])