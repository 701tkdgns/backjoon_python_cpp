import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    L = tuple(map(int, input().split()))
    lst.append(L)
lst.sort()
left, right, res = lst[0][0], lst[0][1], 0
for i in range(len(lst)):
    if right > lst[i][1]:
        continue

    if lst[i][0] <= right < lst[i][1]:
        right = lst[i][1]
    elif right < lst[i][0]:
        res += right - left
        right = lst[i][1]
        left = lst[i][0]
res += right - left
print(res)