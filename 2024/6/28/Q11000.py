import heapq
N = int(input())
subject = []
hq = []
for _ in range(N):
    S, T = map(int, input().split())
    subject.append([S, T])
subject.sort()
heapq.heappush(hq, subject[0][1])
for i in range(1, N):
    if subject[i][0] < hq[0]:
        heapq.heappush(hq, subject[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, subject[i][1])
print(len(hq))