from collections import deque


def bfs(v):
    cnt = 0
    dq = deque([v])
    chk[v] = True
    while dq:
        v = dq.popleft()
        for i in lst[v]:
            if not chk[i]:
                cnt += 1
                dq.append(i)
                chk[i] = True
    return cnt


com_cnt = int(input())
lst = [[] for _ in range(com_cnt + 1)]
chk = [False for _ in range(com_cnt + 1)]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for L in lst:
    L.sort()

print(bfs(1))