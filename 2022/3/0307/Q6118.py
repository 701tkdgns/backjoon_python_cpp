from collections import deque


def bfs(v):
    dq = deque()
    dq.append(v)
    visit[v] = True
    tmp, tmp_idx = 0, 0
    while dq:
        v = dq.popleft()
        for i in lst[v]:
            if not visit[i]:
                chk[i] = chk[v] + 1
                visit[i] = True
                dq.append(i)
            if tmp < chk[i]:
                tmp_idx = i
                tmp = chk[i]
            elif tmp == chk[i]:
                tmp_idx = min(tmp_idx, i)
    return tmp_idx


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
chk = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in lst:
    i.sort()
r_num = bfs(1)

l_num, cnt_num = chk[r_num], 0
for i in chk:
    if chk[r_num] == i:
        cnt_num += 1
print(r_num, l_num, cnt_num)
