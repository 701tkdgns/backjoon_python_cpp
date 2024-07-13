import heapq, sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    s, t = map(int, input().split())
    lst.append([s, t])
lst.sort(key=lambda x: (x[0], x[1]))
hq = []
for s, t in lst:
    if hq and hq[0] <= s:
        heapq.heappop(hq)
        heapq.heappush(hq, t)
    else:
        heapq.heappush(hq, t)
print(len(hq))