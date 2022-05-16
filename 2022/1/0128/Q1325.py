from collections import deque


def init():
    return [False for _ in range(N + 1)]


def bfs(v):
    cnt = 1
    dq = deque([v])
    visit[v] = True
    while dq:
        v = dq.popleft()
        for i in lst[v]:
            if not visit[i]:
                dq.append(i)
                cnt += 1
                visit[i] = True
    return cnt


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
mx, answer = 0, []
for _ in range(M):
    a, b = map(int, input().split())
    lst[b].append(a)
for i in range(1, N + 1):
    visit = init()
    cnt = bfs(i)
    if cnt > mx:
        mx = cnt
    answer.append([i, cnt])
for idx, val in answer:
    if val == mx:
        print(idx, end=' ')
