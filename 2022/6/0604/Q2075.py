import heapq

N = int(input())
hq = []
for _ in range(N):
    lst = list(map(int, input().split()))
    if not hq:
        for tmp in lst:
            heapq.heappush(hq, tmp)
    else:
        for tmp in lst:
            if hq[0] < tmp:
                heapq.heappush(hq, tmp)
                heapq.heappop(hq)
print(hq[0])
