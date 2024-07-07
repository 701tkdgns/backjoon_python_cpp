import heapq
N = int(input())
hq = []
res = 0
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(hq, [s, 1])
    heapq.heappush(hq, [e, -1])
for idx, val in hq:
    res += val
print(res)