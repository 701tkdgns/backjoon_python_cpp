from collections import deque


def bfs():
    pass


N, M = map(int, input().split())
lst = []
visit = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    lst.append(list(map(str, input().split())))

for i in lst:
    print(" ".join(i))