import heapq, sys
input = sys.stdin.readline

N, K = map(int, input().split())
jews, bags = [], []
for _ in range(N):
    M, V = map(int, input().split())
    jews.append([M, V])
for _ in range(K):
    C = int(input())
    bags.append(C)
jews.sort(key=lambda x: (x[0], -x[1]))
bags.sort()
hq = []
res = 0
for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(hq, -jews[0][1])
        heapq.heappop(jews)
    if hq:
        res += -(heapq.heappop(hq))
print(res)
# import heapq
# N, K = map(int, input().split())
# bags, jews = [], []
# for _ in range(N):
#     M, V = map(int, input().split())
#     jews.append([M, V])
# for _ in range(K):
#     C = int(input())
#     bags.append(C)
# bags.sort()
# jews.sort(key=lambda x: (x[0], -x[1]))
# res = 0
# steal_jew = []
# for bag in bags:
#     while jews and bag >= jews[0][0]:
#         heapq.heappush(steal_jew, -jews[0][1])
#         heapq.heappop(jews)
#     if steal_jew:
#         res -= heapq.heappop(steal_jew)
# print(res)
