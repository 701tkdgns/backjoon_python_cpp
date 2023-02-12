n = int(input())
lst = []
greed = {}
g_lst = []

for _ in range(n):
    lst.append(input())

for i in range(n):
    for j in range(len(lst[i])):
        if lst[i][j] in greed:
            greed[lst[i][j]] += 10 ** (len(lst[i]) - j - 1)
        else:
            greed[lst[i][j]] = 10 ** (len(lst[i]) - j - 1)
        print(greed)

for v in greed.values():
    g_lst.append(v)

g_lst.sort(reverse=True)
res = 0
p = 9
for i in g_lst:
    res += (p * i)
    p -= 1
print(res)
