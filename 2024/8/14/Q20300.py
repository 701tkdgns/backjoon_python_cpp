import sys

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = -1
if N % 2 == 1:
    for i in range(N - 1):
        res = max(lst[i] + lst[N - 2 - i], res)
    res = max(res, lst[N - 1])
else:
    for i in range(N):
        res = max(lst[i] + lst[N - 1 - i], res)
print(res)