S = list(map(str, input()))
bomb = list(map(str, input()))
stk = []
for i in range(len(S)):
    stk.append(S[i])
    if stk and stk[-len(bomb):] == bomb:
        cnt = len(bomb)
        while cnt > 0:
            stk.pop()
            cnt -= 1
print(''.join(stk) if stk else "FRULA")