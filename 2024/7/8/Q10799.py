S = input()
stk = []
res = 0
for i in range(len(S)):
    if S[i] == '(':
        stk.append(S[i])
    elif S[i] == ')':
        if S[i - 1] == ')':
            stk.pop()
            res += 1
        elif S[i - 1] == '(':
            stk.pop()
            res += len(stk)
print(res)
