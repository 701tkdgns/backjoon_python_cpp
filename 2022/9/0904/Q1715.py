import heapq

N = int(input())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(input()))
if len(hq) == 1:
    print(0)
else:
    answer = 0
    while len(hq) > 1:
        tmp1 = heapq.heappop(hq)
        tmp2 = heapq.heappop(hq)
        answer += tmp1 + tmp2
        heapq.heappush(hq, tmp1+tmp2)
    print(answer)