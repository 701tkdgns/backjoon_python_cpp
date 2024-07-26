N = int(input())
lst = list(map(int, input().split()))
stk, res = [], [-1 for _ in range(N)]
for i in range(N):
    while stk and lst[stk[-1]] < lst[i]:
        idx = stk.pop()
        res[idx] = lst[i]
    stk.append(i)
print(*res)
