from collections import deque

def bfs():
    global q
    nq = []
    while q:
        v, x, y = q[0]
        del q[0]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0:
                nq.append([lst[x][y], nx, ny])
                lst[nx][ny] = lst[x][y]
    q = nq.copy()

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, K = map(int, input().split())
lst = []
q = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] != 0 and tmp[j] <= K:
            q.append([tmp[j], i, j])
    lst.append(tmp)
S, X, Y = map(int, input().split())
q.sort()
for _ in range(S):
    bfs()
print(lst[X-1][Y-1])