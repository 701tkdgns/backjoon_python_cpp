from collections import deque
import sys

std = sys.stdin
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(dq):
    cnt = 0
    while dq:
        x, y = dq.popleft()
        chk = True
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 0:
                lst[nx][ny] = 1
                dq.append([nx, ny])
                chk = False
        if chk:
            return cnt
        for i in lst:
            print(*i)
        print()
        cnt += 1
    return cnt


M, N = map(int, std.readline().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

d = deque()
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            d.append([i, j])
res = bfs(d)
print(res)