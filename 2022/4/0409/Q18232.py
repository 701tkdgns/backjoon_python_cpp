from collections import deque
import sys


def bfs(v):
    dq = deque()
    dq.append(v)
    chk[v] = 0
    while dq:
        v = dq.popleft()
        direction = [v + 1, v - 1]
        if tel[v]:
            direction += tel[v]
        for n in direction:
            if 0 < n <= N and chk[n] == -1:
                dq.append(n)
                chk[n] = chk[v] + 1
            if n == E:
                return chk[n]


N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
chk = [-1 for _ in range(N + 1)]
tel = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    tel[x].append(y)
    tel[y].append(x)
res = bfs(S)
print(res)
