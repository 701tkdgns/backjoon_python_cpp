n = int(input())
lst = sorted(list(map(int, input().split())))
res = 200000
for i in range(n):
    a, b = lst[i], lst[len(lst)-1-i]
    res = min(res, a+b)
print(res)
