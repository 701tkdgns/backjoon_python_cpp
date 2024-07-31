N = int(input())
p, s = 0, 0  # 많이 / 적게
lst = list(map(int, input().split()))
lst.sort(reverse=True)
if N % 2 == 0:
    p = sum(lst[:N//2])
    s = sum(lst[N//2:])
else:
    p = sum(lst[:N//2 + 1])
    s = sum(lst[N//2 + 1:])
print(s, p)