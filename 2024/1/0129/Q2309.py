def dfs(_res):
    if sum(_res) == 100:
        if not res:
            for i in _res:
                res.append(i)
        return
    else:
        for i in lst:
            if len(_res) < 7 and i not in _res:
                _res.append(i)
                dfs(_res)
                _res.remove(i)


lst = []
res = []
for _ in range(9):
    lst.append(int(input()))
lst.sort()
dfs([])
for i in res:
    print(i)
