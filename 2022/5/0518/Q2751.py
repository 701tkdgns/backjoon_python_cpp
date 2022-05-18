# def qsort(a):
#     if len(a) <= 1:
#         return a
#
#     left, right = list(), list()
#     pivot = a[0]
#     for i in range(1, len(a)):
#         if pivot > a[i]:
#             left.append(a[i])
#         else:
#             right.append(a[i])
#     return qsort(left) + [pivot] + qsort(right)


lst = list()
for _ in range(int(input())):
    lst.append(int(input()))
res = sorted(lst)
print(res)
