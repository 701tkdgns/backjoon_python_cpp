import sys

sys.setrecursionlimit(10 ** 6)


def dfs(n, c):
    for i in lst[n]:
        tmp_n, tmp_c = i
        if dp[tmp_n] == -1:
            dp[tmp_n] = c + tmp_c
            dfs(tmp_n, c + tmp_c)


N = int(input())
lst = [[] for _ in range(N + 1)]
dp = [-1 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, s = map(int, input().split())
    lst[a].append([b, s])
    lst[b].append([a, s])
dp[1] = 0
dfs(1, 0)
idx, tmp_max = 0, 0
for i in range(1, len(dp)):
    if tmp_max < dp[i]:
        idx = i
        tmp_max = dp[i]
dp = [-1 for _ in range(N + 1)]
dp[idx] = 0
dfs(idx, 0)
res = 0
for i in range(1, len(dp)):
    res = max(res, dp[i])
print(res)