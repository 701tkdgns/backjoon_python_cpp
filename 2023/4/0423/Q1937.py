import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    if visit[x][y]: return visit[x][y]
    visit[x][y] = 1
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] > lst[x][y]:
            visit[x][y] = max(visit[x][y], dfs(nx, ny) + 1)
    return visit[x][y]

N = int(input())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visit = [[0 for _ in range(N)] for _ in range(N)]
res = 0
for _ in range(N):
    lst.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        res = max(res, dfs(i, j))
print(res)