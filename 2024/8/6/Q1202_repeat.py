import heapq, sys
input = sys.stdin.readline
N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
jewels = [int(input()) for _ in range(K)]
res, idx = 0, 0
hq = []
bags.sort()
jewels.sort()
for k in range(K):
    jewel = jewels[k]
    while idx < N and bags[idx][0] <= jewel:
        heapq.heappush(hq, -bags[idx][1])
        idx += 1
    if hq:
        res += -(heapq.heappop(hq))
print(res)