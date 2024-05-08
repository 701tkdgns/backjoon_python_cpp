K = int(input())
lst = []
stk = []
for _ in range(K):
    k = int(input())
    if k == 0 and stk:
        stk.pop()
    else:
        stk.append(k)
print(sum(stk) if stk else 0)