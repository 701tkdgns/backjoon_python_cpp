import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if cabbage[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    res = 0

    for _ in range(K):
        i, j = map(int, input().split())
        cabbage[i][j] = 1

    for i in range(M):
        for j in range(N):
            if cabbage[i][j] and not visited[i][j]:
                dfs(i, j)
                res += 1
    print(res)
