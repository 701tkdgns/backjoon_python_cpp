import sys
import heapq

h = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x), x))  # (우선순위, 값)
