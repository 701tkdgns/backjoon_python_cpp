import heapq
lst = []
for i in range(int(input())):
    heapq.heappush(lst, float(input()))
for _ in range(7):
    print('{:.3f}'.format(heapq.heappop(lst)))
