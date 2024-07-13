N, K = map(int, input().split())
NUM = input().rstrip()
stk = []
for i in range(N):
    while stk and stk[-1] < NUM[i] and K > 0:
        stk.pop()
        K -= 1
    stk.append(NUM[i])
res = ''
for i in stk:
    res += i
print(stk[:-K] if K > 0 else res)