N = int(input().rstrip())
res = 0
idx = 1
while True:
    if ((N + 1) * idx) // N >= N:
        break
    else:
        res += ((N + 1) * idx)
    idx += 1
    # print(res)
print(res)
