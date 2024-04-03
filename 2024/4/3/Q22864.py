A, B, C, M = map(int, input().split())
cnt = 24
work, p = 0, 0
while cnt > 0:
    if p + A > M:
        p = 0 if p - C < 0 else p - C
        cnt -= 1
    else:
        p += A
        work += B
        cnt -= 1
print(work)