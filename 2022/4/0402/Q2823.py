from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] == '.':
                cnt += 1
                if not chk[nx][ny]:
                    dq.append([nx, ny])
                    chk[nx][ny] = True
        if cnt < 2:
            return 1
    return 0


R, C = map(int, input().split())
lst = []
chk = [[False for _ in range(C)] for _ in range(R)]
tmp = [[0 for _ in range(C)] for _ in range(R)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(R):
    lst.append(list(input().rstrip()))

tmpx, tmpy = 0, 0
for i in range(R):
    for j in range(C):
        if lst[i][j] == '.' and not chk[i][j]:
            tmpx, tmpy = i, j
            break

print(bfs(tmpx, tmpy))
