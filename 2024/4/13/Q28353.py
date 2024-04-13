N, K = map(int, input().split())
cats = sorted(list(map(int, input().split())))
i, j = 0, N - 1
cnt = 0
while i < j:
    if cats[i] + cats[j] <= K:
        cnt += 1
        i += 1
        j -= 1
    else:
        j -= 1
print(cnt)