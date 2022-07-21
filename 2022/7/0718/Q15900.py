from collections import deque


def bfs(v):
    dq = deque([v])
    visit[v] = True
    while dq:
        v = dq.popleft()
        for idx in lst[v]:
            if not visit[idx]:
                dq.append(idx)
                chk = not chk
                visit[idx] = True
    return chk


N = int(input())
lst = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
stk = [[1, 0]]
for i in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
bfs(1)