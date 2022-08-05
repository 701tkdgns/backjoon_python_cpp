import heapq

def dijkstra():
    pass

N, E = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
v1, v2 = map(int, input().split())