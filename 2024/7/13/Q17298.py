N = int(input())
lst = list(map(int, input().split()))
place = [-1] * N
tmp = []
for idx in range(N):
    while tmp and lst[tmp[-1]] < lst[idx]:
        place[tmp.pop()] = lst[idx]
    tmp.append(idx)
    print(tmp, place)
print(*place)