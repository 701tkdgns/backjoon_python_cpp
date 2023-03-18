from collections import deque


def bfs(init_v):
    global res
    dq = deque([init_v])
    visit[init_v] = 0
    while dq:
        v = dq.popleft()
        if v == K:
            res += 1
            continue
        for new_v in [v + 1, v - 1, v * 2]:
            if 0 <= new_v <= 100000 and (visit[new_v] == -1 or visit[new_v] == visit[v] + 1):
                visit[new_v] = visit[v] + 1
                dq.append(new_v)


N, K = map(int, input().split())
visit = [-1 for _ in range(100001)]
res = 0
bfs(N)
print(visit[K])
print(res)
