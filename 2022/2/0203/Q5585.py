N = int(input())
r = 1000 - N
R = [500, 100, 50, 10, 5, 1]
cnt = 0
while r != 0:
    for i in R:
        if r <= 0:
            break
        if r >= i:
            tmp = r // i
            r -= i * tmp
            cnt += tmp
print(cnt)
