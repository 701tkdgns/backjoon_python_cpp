N, K = map(int, input().split())
V = input()
stk = []
for word in V:
    while stk and int(stk[-1]) < int(word) and K > 0:
        stk.pop()
        K -= 1
    stk.append(word)
if K > 0:
    print(''.join(map(str, stk[:-K])))
else:
    print(''.join(map(str, stk)))