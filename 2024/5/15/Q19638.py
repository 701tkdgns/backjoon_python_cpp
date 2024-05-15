import heapq
import sys
input = sys.stdin.readline

n, h, t = map(int, input().split())
cnt = 0
hq = []
for _ in range(n):
    l = int(input())
    heapq.heappush(hq, -l)
for i in range(t):
    if -hq[0] == 1 or -hq[0] < h:
        break
    else:
        heapq.heapreplace(hq, -(-hq[0] // 2))
        cnt += 1

if -hq[0] >= h:
    print("NO")
    print(-hq[0])
else:
    print("YES")
    print(cnt)
