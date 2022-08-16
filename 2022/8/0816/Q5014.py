import sys
from collections import deque


def bfs(s):
    dq = deque([s])
    visit[s] = 0
    while dq:
        x = dq.popleft()
        if x == G:
            break
        for d in direction:
            nx = x + d
            if 1 <= nx <= F and visit[nx] == -1:
                visit[nx] = visit[x] + 1
                dq.append(nx)


F, S, G, U, D = map(int, sys.stdin.readline().split())
direction = [U, -D]
visit = [-1 for _ in range(F + 1)]
bfs(S)
if visit[G] == -1:
    print("use the stairs")
else:
    print(visit[G])
