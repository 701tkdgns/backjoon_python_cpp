import heapq
from collections import deque
def solution(operations):
    answer = []
    p_hq = []
    m_hq = []
    for s in operations:
        c, v = s.split()
        if c == 'I':
            heapq.heappush(p_hq, int(v))
            heapq.heappush(m_hq, int(v) * -1)
        elif c == 'D':
            if v == '1' and m_hq:
                tmp_v = heapq.heappop(m_hq) * -1
                del p_hq[p_hq.index(tmp_v)]
                heapq.heapify(p_hq)
            elif v == '-1' and p_hq:
                tmp_v = heapq.heappop(p_hq) * -1
                del m_hq[m_hq.index(tmp_v)]
                heapq.heapify(m_hq)
    if not p_hq or not m_hq:
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(m_hq), heapq.heappop(p_hq)]
    return answer