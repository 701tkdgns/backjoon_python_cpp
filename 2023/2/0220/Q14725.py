N = int(input())
lst = []
for _ in range(N):
    s = list(input().split())
    lst.append(s[1:])

lst.sort()

dash = '--'
res = []

for i in range(N):
    if i == 0:
        for j in range(len(lst[i])):
            res.append(dash * j + lst[i][j])
    else:
        idx = 0
        for j in range(len(lst[i])):
            if lst[i-1][j] != lst[i][j] or len(lst[i-1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(lst[i])):
            res.append(dash * j + lst[i][j])


for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end="")
    print()


# for i in range(N):
#     if i == 0:
#         for j in range(len(lst[i])):
#             res.append(dash * j + lst[i][j])
#     else:
#         idx = 0
#         for j in range(len(lst[i])):
#             if lst[i-1][j] != lst[i][j] or len(lst[i-1]) <= j:
#                 break
#             else:
#                 idx = j + 1
#         for j in range(idx, len(lst[i])):
#             res.append(dash * j + lst[i][j])
#
#     for r in res:
#         print(r)
#     print()