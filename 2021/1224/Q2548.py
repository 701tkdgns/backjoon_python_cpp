n = int(input())
lst = list(map(int, input().split()))
lst.sort()

L, R = 0, sum(lst)
res, res_idx = max(lst), 0
for i in range(n):
    L += lst[i]
    R -= lst[i]
    print(lst[i]*(i+1)-L, R-(lst[i]*(n-i-1)))
    tmp = (lst[i]*(i+1) - L) + (R - (lst[i]*(n-i-1)))
    if tmp < res:
        res = tmp

        res_idx = i
print(lst[res_idx])



# import sys
# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# lst.sort()
# mx, res = sum(lst), max(lst)
# for i in lst:
#     SUM = 0
#     for j in lst:
#         SUM += abs(i-j)
#     if mx > SUM:
#         mx = SUM
#         res = i
# print(res)