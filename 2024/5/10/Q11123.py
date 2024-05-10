from collections import deque

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(v1, v2):
    dq = deque([[v1, v2]])
    visit[v1][v2] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and lst[nx][ny] == '#' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dq.append([nx, ny])


for _ in range(int(input())):
    H, W = map(int, input().split())
    lst = [list(map(str, input().rstrip())) for _ in range(H)]
    visit = [[0 for _ in range(W)] for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if lst[i][j] == '#' and visit[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)
