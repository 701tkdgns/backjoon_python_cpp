import sys
input = sys.stdin.readline
S = list(map(str, input().rstrip()))
stk = []
cnt = 0
for idx in range(len(S)):
    if S[idx] == '(':
        stk.append(S[idx])
    elif S[idx] == ')':
        if S[idx - 1] == '(':
            stk.pop()
            cnt += len(stk)
        elif S[idx - 1] == ')':
            stk.pop()
            cnt += 1
print(cnt)