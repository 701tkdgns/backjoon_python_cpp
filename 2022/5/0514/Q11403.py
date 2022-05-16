from collections import deque


def bfs():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if lst[i][k] and lst[k][j]:
                    lst[i][j] = 1


N = int(input())
lst = []
visited = [[False for _ in range(N)] for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(N):
    lst.append(list(map(int, input().split())))
bfs()
print(lst)