import heapq
N, K = map(int, input().split())
lst, bags = [], []
for _ in range(N):
    M, V = map(int, input().split())
    lst.append([M, V])
for _ in range(K):
    c = int(input())
    bags.append(c)
lst.sort(key=lambda x: (x[0], -x[1]))
bags.sort()
hq = []
res = 0
for bag in bags:
    while lst and bag >= lst[0][0]:
        heapq.heappush(hq, -lst[0][1])
        heapq.heappop(lst)
    if hq:
        res -= heapq.heappop(hq)
print(res)