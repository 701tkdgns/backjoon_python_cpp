import heapq, sys
input = sys.stdin.readline

N, K = map(int, input().split())
jews, bags = [], []
for _ in range(N):
    M, V = map(int, input().split())
    jews.append([M, V])
for _ in range(K):
    C = int(input())
    bags.append(C)
jews.sort(key=lambda x: (x[0], -x[1]))
# jews.sort(reverse=True)
bags.sort()
hq = []
res = 0
for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(hq, -jews[0][1])
        heapq.heappop(jews)
    if hq:
        res += -(heapq.heappop(hq))
print(res)