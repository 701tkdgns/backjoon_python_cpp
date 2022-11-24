import heapq
from collections import deque


def dijkstra(init_x, init_y):
    hq = []
    heapq.heappush(hq, [0, 0, init_x, init_y])
    while hq:
        val, d, x, y = heapq.heappop(hq)
        for i in range(4):
            nx, ny = direction[i][0] + x, direction[i][1] + y
            if 0 <= nx < N and 0 <= ny < N:
                

N = int(input())
lst = []
visit = [[-1 for _ in range(N)] for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 0, 1, 2, 3
door, mirror = [], []
for i in range(N):
    lst.append(list(map(str, input().rstrip())))
    for j in range(len(lst[i])):
        if lst[i][j] == "#":
            door.append([i, j])
        if lst[i][j] == "!":
            mirror.append([i, j])

a, b = door.pop()
dijkstra(a, b)
