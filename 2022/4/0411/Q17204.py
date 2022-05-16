from collections import deque


def bfs(v):
    dq = deque([v])
    cnt = 0
    for _ in range(N):
        t = dq.popleft()
        cnt += 1
        if lst[t] == K:
            return cnt
        dq.append(lst[t])
    return -1


N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
print(bfs(0))
