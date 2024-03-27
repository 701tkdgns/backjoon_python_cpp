N = int(input())
visit = [0 for _ in range(N + 1)]
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
while lst:
    tmp = []
    v = lst[-1]
    for i in lst:
        if i not in tmp:
            tmp.append(i)
    for i in tmp:
        del lst[lst.index(i)]
    cnt += 1
print(cnt)