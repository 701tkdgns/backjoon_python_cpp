S = list(map(str, input().rstrip()))
B = list(map(str, input().rstrip()))
stk = []
for i in range(len(S)):
    stk.append(S[i])
    if len(stk) >= len(B):
        if stk[-len(B):] == B:
            cnt = len(B)
            while cnt > 0:
                stk.pop()
                cnt -= 1
print(''.join(stk) if stk else 'FRULA')