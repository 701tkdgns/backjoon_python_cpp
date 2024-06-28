S = input()
stk = []
cnt = 0
for i in range(len(S)):
    if S[i] == "(":
        stk.append(S[i])
    elif S[i] == ")":
        if S[i - 1] == "(":
            stk.pop()
            cnt += len(stk)
        elif S[i - 1] == ")":
            stk.pop()
            cnt += 1
print(cnt)