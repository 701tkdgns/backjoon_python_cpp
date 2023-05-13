def makeTable(p):
    tmp = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j - 1]
        if p[i] == p[j]:
            j += 1
            tmp[i] = j
    return tmp


def kmp(t, p):
    c = 0
    pos = []
    j = 0
    for i in range(len(t)):
        while j > 0 and p[j] != t[i]:
            j = table[j - 1]
        if p[j] == t[i]:
            if i == len(p) - 1:
                c += 1
                pos.append(i - len(p) + 2)
                j = table[j]
            else:
                j += 1
    return c, pos


t = input()
p = input()
table = makeTable(p)
print(table)
cnt, positions = kmp(t, p)
print(cnt)
print(*positions)