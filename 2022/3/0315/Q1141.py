n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
lst.sort(key=lambda x: len(x))
res = 0
for i in range(n):
    chk = True
    for j in range(i + 1, n):
        if lst[j].startswith(lst[i]):
            chk = False
            break
    if chk:
        res += 1
print(res)
