N = int(input())
lst = list(map(int, input().split()))
lst.sort()
origin = sum(lst)
res = 0
for i in lst:
    if i < origin:
        origin -= i
        res += origin * i
print(res)
