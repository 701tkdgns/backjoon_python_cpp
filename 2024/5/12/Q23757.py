import heapq
n, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
hq = []
for i in N:
    heapq.heappush(hq, -i)
res = 1
for i in M:
    v = -heapq.heappop(hq)
    if v - i < 0:
        res = 0
        break
    else:
        heapq.heappush(hq, -(v - i))
print(res)