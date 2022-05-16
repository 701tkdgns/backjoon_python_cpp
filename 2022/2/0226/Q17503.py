import heapq, sys

N, M, K = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(K)]
beers2 = sorted(beers, key = lambda x: (x[1], x[0]))
heap = []
flay_p, cnt, left = 0, 0, 0
for beer in beers2:
    flay_p += beer[0]
    heapq.heappush(heap, beer[0])
    if len(heap) == N:
        if flay_p >= M:
            answer = beer[1]
            break
        else:
            flay_p -= heapq.heappop(heap)
else:
    print(-1)
    exit()
print(answer)