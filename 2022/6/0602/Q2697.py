N = int(input())
lst = []
res = 0
for _ in range(N):
    lst.append(int(input()))
candidate = lst[1:len(lst)]
H = lst[0]
if N == 1:
    print(0)
else:
    num = 0
    candidate = sorted(candidate, reverse=True)
    while candidate[0] >= H:
        H += 1
        candidate[0] -= 1
        num += 1
        candidate = sorted(candidate, reverse=True)
    print(num)