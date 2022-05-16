N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
cnt, chk = 0, False
while not chk:
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1]:
            chk = True
        else:
            chk = False
            break
    if chk:
        break

    for i in range(len(lst)):
        if i != len(lst) - 1:
            while lst[i] >= lst[i + 1]:
                lst[i] -= 1
                cnt += 1
print(cnt)
