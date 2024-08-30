import heapq


def solution(n, works):
    answer = 0
    hq = []
    for v in works:
        heapq.heappush(hq, -v)
    while (n > 0):
        v = heapq.heappop(hq)
        if v == 0: break
        v += 1
        heapq.heappush(hq, v)
        n -= 1

    for v in hq:
        answer += (v * -1) ** 2
    return answer