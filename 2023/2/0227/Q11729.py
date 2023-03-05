def hanoi(_n, _from, _by, _to):
    if _n == 1:
        lst.append([_from, _to])
        return
    hanoi(_n - 1, _from, _to, _by)
    lst.append([_from, _to])
    hanoi(_n - 1, _by, _from, _to)


n = int(input())
k = 2 ** n - 1
lst = []
hanoi(n, 1, 2, 3)
print(k)
for i, j in lst:
    print(i, j)