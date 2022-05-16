N, M = int(input()), int(input())
lst = list(map(int, input().split()))
chk = [False for _ in range(N)]
start, end, cnt = 0, N-1, 0
lst.sort()
while start < end:
    if M > lst[start] + lst[end]:
        start += 1
    elif M < lst[start] + lst[end]:
        end -= 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)
