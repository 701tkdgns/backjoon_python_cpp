N = int(input())
lst = sorted(list(map(int, input().split())))
idx = 0
if N % 2 == 0:
    idx = N // 2 - 1
else:
    idx = N // 2
print(lst[idx])