from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and lst[nx][ny] == 1:
                dq.append([nx, ny])
                visit[nx][ny] = True


n, m = map(int, input().split())
lst = []
cnt = 0
visit = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if not visit[i][j] and lst[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)