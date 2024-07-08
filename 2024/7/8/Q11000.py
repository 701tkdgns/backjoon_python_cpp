import heapq, sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    s, t = map(int, input().split())
    lst.append([s, t])
lst.sort(key=lambda x: (x[0], x[1]))
hq = [lst[0][1]]
for idx in range(1, len(lst)):
    if hq[0] > lst[idx][0]:
        heapq.heappush(hq, lst[idx][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, lst[idx][1])

print(len(hq))
