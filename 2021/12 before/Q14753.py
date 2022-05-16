import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
lst2 = [lst[0]*lst[1], lst[0]*lst[-1], lst[-2]*lst[-1]]
lst3 = [lst[-3]*lst[-2]*lst[-1], lst[0]*lst[-2]*lst[-1], lst[0]*lst[1]*lst[-1], lst[0]*lst[1]*lst[2]]
print(max(max(lst2), max(lst3)))











# for i in range(len(lst)-2):
#     for j in range(i+1, len(lst)-1):
#         for k in range(j+1, len(lst)):
#             mx = max(lst[i]*lst[j]*lst[k], max(lst[i]*lst[j], lst[j]*lst[k]))
# print(mx)
# lst_thr.append(lst[i]*lst[j]*lst[k])
# for i in range(len(lst)-1):
#     for j in range(i+1, len(lst)):
#         lst_two.append(lst[i]*lst[j])
# print(max(max(lst_two), max(lst_thr)))