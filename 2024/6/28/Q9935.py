S = input()
bomb = list(input())
stk = []
for i in range(len(S)):
    stk.append(S[i])
    if stk[-1] == bomb[-1]:
        if len(bomb) <= len(stk):
            if stk[-len(bomb):] == bomb:
                for _ in range(len(bomb)):
                    stk.pop()
print(''.join(stk) if stk else "FRULA")