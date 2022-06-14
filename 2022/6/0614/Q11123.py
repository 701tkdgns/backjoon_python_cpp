from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visit[nx][ny] and lst[nx][ny] == '#':
                dq.append([nx, ny])
                visit[nx][ny] = True


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    lst = []
    visit = [[False for _ in range(W)] for _ in range(H)]
    cnt = 0
    for _ in range(H):
        tmp = list(map(str, input().rstrip()))
        lst.append(tmp)
    for i in range(H):
        for j in range(W):
            if not visit[i][j] and lst[i][j] == '#':
                bfs(i, j)
                cnt += 1
    print(cnt)