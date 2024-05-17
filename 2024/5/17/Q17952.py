import sys
input = sys.stdin.readline
N = int(input())
stk = []
res = 0
for i in range(N):
    subject = list(map(int, input().split()))
    if subject[0] == 0:
        if stk:
            score, time = stk.pop()
            if time - 1 > 0:
                time -= 1
                stk.append([score, time])
            else:
                res += score
    else:
        score, time = subject[1], subject[2]
        if time - 1 > 0:
            time -= 1
            stk.append([score, time])
        else:
            res += score
print(res)