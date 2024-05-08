from collections import deque
T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    flag = 1
    lst = input().rstrip()
    dq = deque(lst[1:-1].split(","))
    if n == 0:
        dq = deque()
    R = 0
    for i in range(len(p)):
        if p[i] == "R":
            R += 1
        else:
            if len(dq) == 0:
                print("error")
                flag = 0
                break
            else:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    if flag == 0:
        continue
    else:
        if R % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")