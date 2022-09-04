import sys
std = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(v):
    cnt[v] = 1
    for i in lst[v]:
        if cnt[i] == 0:
            dfs(i)
            cnt[v] += cnt[i]


N, R, Q = map(int, std().split())
lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, std().split())
    lst[a].append(b)
    lst[b].append(a)
cnt = [0 for _ in range(N + 1)]
dfs(R)
for _ in range(Q):
    U = int(std())
    print(cnt[U])
