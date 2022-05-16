import heapq, sys
std = sys.stdin
N, M, K = map(int, std.readline().split()) # n : 기간, m : 선호도 합, k : 맥주 종류
lst, pq = [], []
heapq.heapify(pq)
for _ in range(K):
    v, c = map(int, std.readline().split())
    lst.append([v, c])
lst.sort(key=lambda x:(x[1],x[0]))
chk = False
alch, s = 0, 0
for i in range(K):
    heapq.heappush(pq, lst[i][0])
    s += lst[i][0]
    alch = lst[i][1]
    if len(pq) == N:
        if s >= M:
            chk = True
            break
        else:
            s -= heapq.heappop(pq)
if not chk:
    print(-1)
else:
    print(alch)