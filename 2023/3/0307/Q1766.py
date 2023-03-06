import heapq

hq, res = [], []
N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    visit[b] += 1

print(visit)

for i in range(1, N + 1):
    if visit[i] == 0:
        heapq.heappush(hq, i)

while hq:
    tmp = heapq.heappop(hq)
    res.append(tmp)
    for i in lst[tmp]:
        visit[i] -= 1
        if visit[i] == 0:
            heapq.heappush(hq, i)
print(" ".join(map(str, res)))