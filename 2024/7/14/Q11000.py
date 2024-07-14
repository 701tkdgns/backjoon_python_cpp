import heapq, sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    s, t = map(int, input().split())
    lst.append([s, t])
lst.sort(key=lambda x:(x[0], x[1]))
hq = [lst[0][1]]
for i in range(1, N):
    if lst[i][0] < hq[0]:
        heapq.heappush(hq, lst[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, lst[i][1])
print(len(hq))