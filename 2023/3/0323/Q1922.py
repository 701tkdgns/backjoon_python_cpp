import heapq

def dijkstra():
    hq = []
    heapq.heappush(hq, [0, 1])
    while hq:
        wei, node = heapq.heappop(hq)
        if

N = int(input())
M = int(input())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
dijkstra()