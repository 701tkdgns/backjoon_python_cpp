from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        if x == N - 1 and y == M - 1:
            chk[x][y] += 1
            break
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visit[nx][ny]:
                dq.append([nx, ny])
                visit[nx][ny] = True
                chk[nx][ny] = chk[x][y] + 1


N, M = map(int, input().split())  # 1 이동가능 0 이동 불가능
maze, visit = [], [[False for _ in range(M)] for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
chk = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    maze.append(list(map(int, input().rstrip())))
bfs(0, 0)
print(chk[N-1][M-1])

# https://www.acmicpc.net/problem/2178