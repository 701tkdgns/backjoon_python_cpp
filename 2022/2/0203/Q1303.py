from collections import deque


def bfs(x, y, color):
    cnt = 1
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and war_map[nx][ny] == color and not visit[nx][ny]:
                dq.append([nx, ny])
                visit[nx][ny] = True
                cnt += 1
    return cnt * cnt


N, M = map(int, input().split())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visit = [[False for _ in range(N)] for _ in range(M)]
war_map = []
W, B = 0, 0
for i in range(M):
    war_map.append(list(input().rstrip()))
for i in range(M):
    for j in range(N):
        if war_map[i][j] == 'W' and not visit[i][j]:
            W += bfs(i, j, war_map[i][j])
        elif war_map[i][j] == 'B' and not visit[i][j]:
            B += bfs(i, j, war_map[i][j])
print(W, B)
