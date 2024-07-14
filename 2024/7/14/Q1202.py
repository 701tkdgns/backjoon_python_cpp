import heapq, sys
input = sys.stdin.readline
N, K = map(int, input().split())
bags, stores = [], []
for _ in range(N):
    m, v = map(int, input().split())
    bags.append([m, v])
for _ in range(K):
    c = int(input())
    stores.append(c)
hq = []
res = 0
bags.sort()
stores.sort()
for c in stores:
    while bags and bags[0][0] <= c:
        heapq.heappush(hq, -bags[0][1])
        heapq.heappop(bags)
    if hq:
        res += -(heapq.heappop(hq))
print(res)