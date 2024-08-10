# L은 R의 사전 기술, S은 K의 사전 기술

N = int(input())
skills = input()
SK, LR = [], []
res = 0
for s in skills:
    if 49 <= ord(s) <= 58:
        res += 1
    else:
        if s == 'S':

            SK.append(s)
        if s == 'L':
            LR.append(s)
        if s == 'K':
            if SK:
                SK.pop()
                res += 1
            else:
                break
        if s == 'R':
            if LR:
                LR.pop()
                res += 1
            else:
                break
print(res)