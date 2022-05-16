from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    chk[x][y] = True
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if m[nx][ny] == 'P' and not chk[nx][ny]:
                    cnt += 1
                    dq.append([nx, ny])
                    chk[nx][ny] = True
                elif m[nx][ny] != 'X' and not chk[nx][ny]:
                    dq.append([nx, ny])
                    chk[nx][ny] = True
    return cnt


N, M = map(int, input().split())
m = []  # O 빈공간 X 벽 I 도연 P 사람
chk = [[False for _ in range(M)] for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ix, iy = 0, 0
for i in range(N):
    lst = list(input().rstrip())
    if 'I' in lst:
        ix, iy = i, lst.index('I')
    m.append(lst)

res = bfs(ix, iy)
if res == 0:
    print('TT')
else:
    print(res)
