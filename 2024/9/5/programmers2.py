from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 != 0:
        return -1
    target = (sum1 + sum2) // 2
    max_cnt = len(queue1) * 2 + len(queue2) * 2
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    while answer <= max_cnt:
        if sum1 == target:
            return answer
        if sum1 > target:
            v = dq1.popleft()
            sum1 -= v
            dq2.append(v)
            sum2 += v
        else:
            v = dq2.popleft()
            sum2 -= v
            dq1.append(v)
            sum1 += v
        answer += 1;
    return -1

# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3