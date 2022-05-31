n = int(input())
ABC = [300, 60, 10]
res = [0, 0, 0]
for i in range(3):
    if n >= ABC[i]:
        res[i] = n // ABC[i]
        n = n % ABC[i]
if n != 0:
    print(-1)
else:
    print(*res)
