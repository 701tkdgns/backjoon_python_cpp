from collections import deque

def bfs(_x, _y):
    dq = deque([[_x, _y]])
    visit[_x][_y] = 1
    while dq:
        x, y = dq.popleft()
        if lst[x][y] == -1:
            return True
        direction = [[lst[x][y], 0], [0, lst[x][y]]]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dq.append([nx, ny])
    return False

N = int(input())
lst = []
visit = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    lst.append(list(map(int, input().split())))
res = bfs(0, 0)
print('HaruHaru' if res else 'Hing')