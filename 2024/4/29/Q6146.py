import sys
from collections import deque
input = sys.stdin.readline

def bfs(init_x, init_y):
    dq = deque([])
    dq.append([init_x, init_y])
    visit[init_x][init_y] = 0
    while dq:
        x, y = dq.popleft()
        if x == 500 + X and y == 500 + y:
            break
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 1000 and 0 <= ny < 1000 and lst[nx][ny] != 1 and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                dq.append([nx, ny])


X, Y, N = map(int, input().split())
lst = [[0 for _ in range(1001)] for _ in range(1001)]
visit = [[-1 for _ in range(1001)] for _ in range(1001)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(N):
    a, b = map(int, input().split())
    lst[a + 500][b + 500] = 1
bfs(500, 500)
print(visit[X+500][Y+500])