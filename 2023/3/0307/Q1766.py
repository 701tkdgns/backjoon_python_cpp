import heapq

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
res, hq = [], []

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    visit[b] += 1

for i in range(1, N + 1):
    if visit[i] == 0:
        heapq.heappush(hq, i)

while hq:
    v = heapq.heappop(hq)
    res.append(v)
    for s in lst[v]:
        visit[s] -= 1
        if visit[s] == 0:
            heapq.heappush(hq, s)

print(' '.join(map(str, res)))
