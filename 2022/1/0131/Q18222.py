def recursion(K):
    if K == 0:
        return 0
    if K == 1:
        return 1
    if K % 2 == 1:
        return 1 - recursion(K // 2)
    else:
        return recursion(K // 2)


K = int(input())
res = recursion(K-1)
print(res)













# def recursion(k):
#     if k == 0:
#         return 0
#     if k == 1:
#         return 1
#     if k % 2 == 1:
#         return 1 - recursion(k//2)
#     else:
#         return recursion(k//2)
#
#
# K = int(input())
# print(recursion(K-1))