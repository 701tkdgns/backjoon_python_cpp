from collections import deque


def bfs():
    dq = deque([[0, 1]])
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y] + 1
                dq.append([nx, ny])


N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst[0][0], lst[0][1] = 1, 1
direction = [(1, 0), (0, 1), (1, 1)]
bfs()
print(lst)