from collections import deque


def bfs(init_x, chk):
    dq = deque([init_x])
    visit[init_x] = chk
    while dq:
        x = dq.popleft()
        for idx in lst[x]:
            if not visit[idx]:
                visit[idx] = -1 * visit[x]
                dq.append(idx)
            elif visit[idx] == visit[x]:
                return False
    return True


K = int(input())
for _ in range(K):
    v, e = map(int, input().split())
    lst = [[] for _ in range(v + 1)]
    visit = [False for _ in range(v + 1)]
    res = True
    for _ in range(e):
        u, v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)
    for e in lst:
        e.sort()

    for i in range(1, v + 1):
        if not visit[i]:
            res = bfs(i, 1)
            if not res:
                break

    print("YES" if res else "NO")
