import heapq

T = int(input())
for _ in range(T):
    Q = int(input())
    min_hq, max_hq = [], []
    for _ in range(Q):
        O, N = input().split()
        N = int(N)

        if O == "I":
            heapq.heappush(min_hq, [N, N])
            heapq.heappush(max_hq, [-N, N])
        else:
            if N == 1:
                heapq.heappop(max_hq)
            else:
                heapq.heappop(min_hq)

    print(max_hq, min_hq)