from collections import deque


def bfs(x):
    dq = deque([x])
    distance[x] = 0
    visit[x] = True
    while dq:
        x = dq.popleft()
        for i in lst[x]:
            if not visit[i]:
                visit[i] = True
                dq.append(i)
                distance[i] = distance[x] + 1
                if distance[i] == K:
                    res.append(i)


N, M, K, X = map(int, input().split())  # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
lst = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
distance = [0] * (N+1)
res = []
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
bfs(X)
if not res:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)
