import heapq
import sys

lst = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst)[1])
    else:
        heapq.heappush(lst, (-x, x))