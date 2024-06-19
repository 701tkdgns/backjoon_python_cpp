M, N = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 0
x, y, idx = 0, 0, 0
for _ in range(M * N - 1):
    graph[x][y] = 1
    nx, ny = x + direction[idx][0], y + direction[idx][1]
    if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
        x, y = nx, ny
    else:
        idx = (idx + 1) % 4
        x, y = x + direction[idx][0], y + direction[idx][1]
        cnt += 1
print(cnt)