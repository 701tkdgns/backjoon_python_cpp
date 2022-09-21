from collections import deque


def bfs(v):
    dq = deque([[v, 0]])
    visit[v] = True
    while dq:
        v, cnt = dq.popleft()
        if v == 100:
            return cnt
        for i in direction:
            dx = v + i
            if dx <= 100:
                for node in lst[dx]:
                    if node != 0:
                        if node <= 100 and not visit[node]:
                            visit[node] = True
                            dq.append([node, cnt + 1])
                    else:
                        if dx <= 100 and not visit[dx]:
                            visit[dx] = True
                            dq.append([dx, cnt + 1])


N, M = map(int, input().split())
lst = [[0] for _ in range(101)]
visit = [False for _ in range(101)]
direction = [6, 5, 4, 3, 2, 1]
for _ in range(N + M):
    x, y = map(int, input().split())
    lst[x][0] = y
res = bfs(1)
print(res)
