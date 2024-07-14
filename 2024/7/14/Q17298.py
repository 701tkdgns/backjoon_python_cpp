import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
stk = []
res = [-1] * N
for i in range(N):
    while stk and lst[stk[-1]] < lst[i]:
        res[stk.pop()] = lst[i]
    stk.append(i)
print(*res)