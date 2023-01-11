import heapq

N = int(input())

# leftHeap은 최대힙으로, rightHeap은 최소힙
# 최대힙 : 역정렬
# 최소힙 : 정렬
left, right = [], []

for _ in range(N):
    n = int(input().split())

    if len(left) == len(right):
        heapq.heappush(left, -n)
    else:
        heapq.heappush(right, n)

    if right and right[0] < -left[0]:
        L, R = heapq.heappop(left), heapq.heappop(right)
        heapq.heappush(left, -R)
        heapq.heappush(right, -L)
    print(-left[0])