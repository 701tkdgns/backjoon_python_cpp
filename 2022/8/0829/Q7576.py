from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy


N, M = map(int, input().split())
lst = []
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(M):
    lst.append(list(map(int, input().split())))
for i in lst:
    print(i)
