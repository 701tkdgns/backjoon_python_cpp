S = input()
bomb = list(input())
stk = []
for i in range(len(S)):
    stk.append(S[i])
    if stk[-len(bomb):] == bomb:
        for idx in range(len(bomb)):
            stk.pop()
if stk:
    print(''.join(stk))
else:
    print('FRULA')