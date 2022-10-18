import sys

sys.setrecursionlimit(10 ** 5)


def dfs(x, y):
    if x == R - 1 and y == C - 1 and visit[x][y] == K:
        res.append([x, y])

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == -1 and lst[nx][ny] == ".":
            visit[nx][ny] = visit[x][y] + 1
            dfs(nx, ny)


R, C, K = map(int, input().split())
lst = []
res = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(R):
    lst.append(list(map(str, input().rstrip())))
visit = [[-1 for _ in range(C)] for _ in range(R)]
visit[0][0] = 0
dfs(0, 0)
print(res)
for i in visit:
    print(*i)
