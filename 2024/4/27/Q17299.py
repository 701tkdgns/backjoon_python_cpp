N = int(input())
lst = list(map(int, input().split()))
od = dict()
stk = []
res = [-1 for _ in range(N)]
for i in lst:
    od[i] = od.get(i, 0) + 1
for i in range(N):
    print(i, stk, "front")
    while stk and od[lst[stk[-1]]] < od[lst[i]]:
        res[stk.pop()] = lst[i]
        print(i, lst[i], stk, res, "back")
    stk.append(i)
print(res)