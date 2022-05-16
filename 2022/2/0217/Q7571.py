N, M = map(int, input().split())
X, Y = [], []
for _ in range(M):
    i, j = map(int, input().split())
    X.append(i)
    Y.append(j)
X.sort()
Y.sort()
x, y = X[M//2], Y[M//2]
res = 0
for i in range(M):
    res += abs(x-X[i])+abs(y-Y[i])
print(res)

# lst = [1, 2, 3, 4, 5]
#
# for i in range(len(lst)):
#     for j in range(i, len(lst)):
#         for k in range(i, j+1):
#             print(lst[k], end=' ')
#         print()