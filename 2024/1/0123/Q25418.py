A, K = map(int, input().split())
cnt = 0
while 1:
    if A == K:
        print(cnt)
        break
    if K % 2 == 0 and K >= A * 2:
        K = K // 2
    else:
        K -= 1
    cnt += 1