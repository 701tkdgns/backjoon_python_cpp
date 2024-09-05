from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    timer = deque()
    dq = deque(truck_weights)
    while dq:
        while timer and q and timer[0] == bridge_length:
            timer.popleft()
            q.popleft()
        v = dq.popleft()
        if len(q) < bridge_length and sum(q) + v <= weight :
            q.append(v)
            timer.append(0)
        else:
            dq.appendleft(v)
        for i in range(len(timer)):
            timer[i] += 1
        answer += 1

    while timer and q:
        while timer and q and timer[0] == bridge_length:
            timer.popleft()
            q.popleft()
        for i in range(len(timer)):
            timer[i] += 1
        answer += 1
    return answer