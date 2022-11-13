from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if lst[nx][ny] != 0:
                    visit[nx][ny] = True
                    dq.append([nx, ny])
                elif lst[nx][ny] == 0 and lst[x][y] > 0:
                    lst[x][y] -= 1

    return 1
N, M = map(int, input().split())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
res,cnt = 0, 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

while True:
    cnt = 0
    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and lst[i][j] != 0:
                cnt += bfs(i, j)
    if cnt >= 2 or cnt == 0:
        break
    res += 1
if cnt == 0:
    print(0)
else:
    print(res)