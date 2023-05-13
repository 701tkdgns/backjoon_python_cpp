# https://bowbowbow.tistory.com/6
# https://hooongs.tistory.com/305

def makeTable(p):
    j = 0
    tmp = [0 for _ in range(len(p))]
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j - 1]
        if p[i] == p[j]:
            j += 1
            tmp[i] = j
    return tmp


def kmp(s, p):
    cnt = 0
    j = 0
    pos = []
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            print(table, j, 3)
            j = table[j - 1]
            print(table, j, 3)
        if s[i] == p[j]:
            if j == len(p) - 1:
                cnt += 1
                pos.append(i - len(p) + 2)
                j = table[j]
                print(table, j, 2)
            else:
                j += 1
                print(table, j, 1)
    return cnt, pos


S = input()
P = input()
table = makeTable(P)
res, positions = kmp(S, P)
print(res)
print(*positions)