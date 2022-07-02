import sys
std = sys.stdin

N = int(std.readline())
lst, stk = [], []
res = 0
for _ in range(N):
    lst.append(int(std.readline()))
for i in range(N):
    while stk and stk[-1] <= lst[i]:
        stk.pop()
    stk.append(lst[i])
    res += len(stk) - 1
print(res)