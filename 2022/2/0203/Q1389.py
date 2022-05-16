from collections import deque


def bfs(v):
    num = [0 for _ in range(N + 1)]
    dq = deque()
    dq.append(v)
    visit = [v]
    while dq:
        v = dq.popleft()
        for idx in friends[v]:
            if idx not in visit:
                dq.append(idx)
                visit.append(idx)
                num[idx] = num[v] + 1
    return sum(num)


N, M = map(int, input().split())
friends = [[] for _ in range(N + 1)]
res = []
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
for i in friends:
    i.sort()
for i in range(1, N + 1):
    res.append((bfs(i), i))
res.sort(key=lambda x: (x[0], x[1]))
print(res[0][1])
