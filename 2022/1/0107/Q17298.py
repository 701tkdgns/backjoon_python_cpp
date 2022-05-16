N = int(input())
lst = list(map(int, input().split()))
stk = []
idx = 0
for i in range(N):
    while stk and lst[stk[-1]] < lst[i]:
        lst[stk.pop()] = lst[i]
    stk.append(i)
while stk:
    lst[stk.pop()] = -1
for i in lst:
    print(i, end=' ')
