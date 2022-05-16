N, M = map(int, input().split())  # 세로 : n, 가로 : m
cnt = 0
if N == 1:
    cnt = 1
elif N == 2:
    cnt = min(4, (M + 1) // 2)
else:
    if M <= 6:
        cnt = min(4, M)
    else:
        cnt = M - 7 + 5
print(cnt)

# https://lipcoder.tistory.com/94