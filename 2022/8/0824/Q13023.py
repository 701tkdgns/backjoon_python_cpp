import sys

sys.setrecursionlimit(10 ** 6)
std = sys.stdin


def dfs(idx, depth):
    global ans
    visit[idx] = True
    if depth == 4:
        ans = True
        return

    for i in lst[idx]:
        if not visit[i]:
            visit[i] = True
            dfs(i, depth + 1)
            visit[i] = False


N, M = map(int, std.readline().split())
lst = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, std.readline().split())
    lst[a].append(b)
    lst[b].append(a)
for e in lst:
    e.sort()
ans = False
for i in range(N):
    dfs(i, 0)
    visit[i] = False
    if ans:
        break
if ans:
    print(1)
else:
    print(0)