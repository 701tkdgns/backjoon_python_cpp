N, M = map(int, input().split())
pBooks, nBooks = [0 for _ in range(10001)], [0 for _ in range(10001)]
lst = list(map(int, input().split()))
lst.sort()
idx, res = 0, 0
for i in lst:
    if i < 0:
        idx += 1

for i in range(N - 1, idx - 1, -M):
    res += abs(lst[i] * 2)

for i in range(0, idx, +M):
    res += abs(lst[i] * 2)

res -= max(abs(lst[0]), abs(lst[N-1]))

print(res)

# https://bba-dda.tistory.com/12
# https://gusdnr69.tistory.com/241