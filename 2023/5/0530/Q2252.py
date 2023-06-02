from collections import deque
N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
inDegree = [0 for _ in range(N + 1)]
dq = deque()
res = []
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    inDegree[b] += 1
for i in range(1, N + 1):
    if inDegree[i] == 0:
        dq.append(i)
while dq:
    v = dq.popleft()
    res.append(v)
    for i in lst[v]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            dq.append(i)
print(*res)