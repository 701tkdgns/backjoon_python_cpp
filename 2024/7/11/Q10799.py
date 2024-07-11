S = input()
stk = []
cnt = 0
for idx in range(len(S)):
    if S[idx] == '(':
        stk.append(S[idx])
    else:
        if S[idx - 1] == '(':
            stk.pop()
            cnt += len(stk)
        elif S[idx - 1] == ')':
            stk.pop()
            cnt += 1
print(cnt)