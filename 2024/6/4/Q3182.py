from collections import deque

def bfs(V):
    global res, res_idx
    dq = deque([V])
    visit[V] = 1
    cnt = 1
    while dq:
        v = dq.popleft()
        for idx in lst[v]:
            if visit[idx] == 0:
                dq.append(idx)
                visit[idx] = 1
                cnt += 1
    if res < cnt:
        res_idx = V
        res = cnt

N = int(input())
lst = [[] for _ in range(N + 1)]
res, res_idx = 0, 0
for i in range(1, N + 1):
    n = int(input())
    lst[i].append(n)

for i in range(1, N + 1):
    visit = [0 for _ in range(N + 1)]
    bfs(i)
print(res_idx)