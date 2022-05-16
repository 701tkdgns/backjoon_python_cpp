def clocknum(n):
    ret = n
    for _ in range(3):
        n = n % 1000 * 10 + n // 1000
        ret = min(ret, n)
    return ret


lst = list(input().split())
rs, cnt = 9999, 0
for i in range(4):
    rs = min(rs, int(lst[i % 4] + lst[(i + 1) % 4] + lst[(i + 2) % 4] + lst[(i + 3) % 4]))
num = []
for i in range(1111, rs+1):
    if clocknum(i) == i:
        cnt += 1
print(cnt)
