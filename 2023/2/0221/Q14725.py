lst = []
res = []
for _ in range(int(input())):
    tmp = list(input().split())
    lst.append(tmp[1:])
lst.sort()
dash = '--'
for i in range(len(lst)):
    if i == 0:
        for j in range(len(lst[i])):
            res += (dash * j) + lst[i][j] + "\n"
    else:
        idx = 0
        for j in range(len(lst[i])):
            if lst[i][j] != lst[i-1][j] or len(lst[i-1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(lst[i])):
            res += (dash * j) + lst[i][j] + "\n"
print(res)