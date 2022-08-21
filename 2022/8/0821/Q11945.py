N, M = map(int, input().split())
lst = []
for _ in range(N):
    tmp = input()
    tmp_r = []
    for i in range(len(tmp)-1, -1, -1):
        tmp_r.append(tmp[i])
    lst.append(tmp_r)
for i in lst:
    print("".join(i))