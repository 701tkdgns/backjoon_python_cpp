import heapq

n = int(input())
hq = []
lst = []
for _ in range(n):
    p, d = map(int, input().split())
    lst.append([d, p])
lst.sort()
for day, pay in lst:
    heapq.heappush(hq, pay)
    if len(hq) > day:
        heapq.heappop(hq)
print(sum(hq))
