import sys

sys.setrecursionlimit(10 ** 6)


def dfs(X):
    visit[X] = True
    min_p = N[X]
    for nxt in lst[X]:
        if visit[nxt] == 1:
            continue
        min_p = min(min_p, dfs(nxt))
    return min_p


n, m, k = map(int, input().split())
N = list(map(int, input().split()))
lst = [[] for _ in range(n)]
visit = [0 for _ in range(n)]
cnt = 0
for _ in range(m):
    v, w = map(int, input().split())
    lst[v - 1].append(w - 1)
    lst[w - 1].append(v - 1)
for i in range(n):
    if visit[i] == 0:
        cnt += dfs(i)
print(cnt if cnt <= k else "Oh no")
