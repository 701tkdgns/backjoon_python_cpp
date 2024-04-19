import sys
from collections import deque
input = sys.stdin.readline

def bfs(_x, _y):
    dq = deque([])
    dq.append([_x, _y])
    visit[_x][_y] = 1
    cnt = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3 and visit[nx][ny] == 0 and lst[nx][ny] == 'O':
                visit[nx][ny] = 1
                dq.append([nx, ny])
                cnt += 1
    return cnt


T = int(input())
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(T):
    lst, res = [], []
    visit = [[0 for _ in range(3)] for _ in range(3)]
    for _ in range(3):
        lst.append(list(input().rstrip()))
    N = list(map(int, input().split()))
    n = N[0]
    del N[0]
    for i in range(3):
        for j in range(3):
            if lst[i][j] == 'O' and visit[i][j] == 0:
                tmp = bfs(i, j)
                res.append(tmp)
    res.sort()
    if n == len(res):
        chk = True
        for i in range(n):
            if N[i] != res[i]:
                chk = False
                break
        print(1 if chk else 0)
    else:
        print(0)