S = list(input())
stk = []
tmp, res, chk = 1, 0, True
for i in range(len(S)):
    if S[i] == '(':
        stk.append(S[i])
        tmp *= 2
    elif S[i] == '[':
        stk.append(S[i])
        tmp *= 3
    elif S[i] == ')' and (not stk or stk[-1] != '('):
        chk = False
        break
    elif S[i] == ']' and (not stk or stk[-1] != '['):
        chk = False
        break
    elif S[i] == ')':
        if S[i - 1] == '(':
            res += tmp
        stk.pop()
        tmp //= 2
    elif S[i] == ']':
        if S[i - 1] == '[':
            res += tmp
        stk.pop()
        tmp //= 3

if not chk or stk:
    print(0)
else:
    print(res)
