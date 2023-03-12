import sys

input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append([int(input()), i])
_lst = sorted(lst)
res = -1
for i in range(N):
    res = max(res, _lst[i][1] - lst[i][1])
print(res + 1)