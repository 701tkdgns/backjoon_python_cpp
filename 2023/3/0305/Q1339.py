n = int(input())
greedy = {}
lst = []
g = []
for _ in range(n):
    v = input()
    lst.append(v)

for i in range(n):
    for j in range(len(lst[i])):
        if lst[i][j] in greedy:
            greedy[lst[i][j]] += 10 ** (len(lst[i]) - j - 1)
        else:
            greedy[lst[i][j]] = 10 ** (len(lst[i]) - j - 1)
for k in greedy:
    g.append(greedy.get(k))
g.sort(reverse=True)
res = 0
cnt = 9
for i in g:
    res += (cnt * i)
    cnt -= 1
print(res)