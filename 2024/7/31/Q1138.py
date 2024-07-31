N = int(input())
lst = list(map(int, input().split()))
res = [0 for _ in range(N)]
stk = []
print(lst)
for i in range(N):
    while stk and lst[stk[-1]] < lst[i]:
        idx = stk.pop()
        res[idx] = idx
    stk.append(i)
# res = '4 2 1 3'
print(res)