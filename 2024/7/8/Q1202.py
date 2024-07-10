import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
bags, inventory = [], []
for _ in range(N):
    m, v = map(int, input().split())
    bags.append([m, v])
for _ in range(K):
    c = int(input())
    inventory.append(c)
bags.sort()
# bags.sort(key=lambda x: (-x[1], x[0]))
inventory.sort()
res = 0
hq = []
for c in inventory:
    while bags and c >= bags[0][0]:
        heapq.heappush(hq, -bags[0][1])
        heapq.heappop(bags)
    if hq:
        res += -(heapq.heappop(hq))
print(res)