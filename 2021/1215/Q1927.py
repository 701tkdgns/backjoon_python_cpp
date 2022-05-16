import heapq
import sys
N = int(sys.stdin.readline())
h = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, x)
