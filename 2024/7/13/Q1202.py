import heapq, sys
input = sys.stdin.readline

N, K = map(int, input().split())
bags, carat = [], []
for _ in range(N):
    m, v = map(int, input().split())
    bags.append([m, v])
for _ in range(K):
    c = int(input())
    carat.append(c)
bags.sort()
carat.sort()
hq = []
res = 0
for c in carat:
    while bags and bags[0][0] <= c:
        heapq.heappush(hq, -bags[0][1])
        heapq.heappop(bags)
    if hq:
        res += -heapq.heappop(hq)
print(res)