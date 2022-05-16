import heapq
lst = []
while True:
    try:
        N = int(input())
        heapq.heappush(lst, (-N, N))
    except EOFError:
        break

while lst:
    print(heapq.heappop(lst)[1])