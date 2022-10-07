N = int(input())
S = input()

cnt = [1, 1]

for i in range(n):
    if arr[i] == 'B':
        continue
    elif arr[i] == 'R':
        cnt[0] += 1
        if arr[i+1] == 'R':
            cnt[0] -= 1
            continue

for i in range(n):
    if arr[i] == 'R':
        continue
    elif arr[i] == 'B':
        cnt[1] += 1
        if arr[i+1] == 'B':
            cnt[1] -= 1
            continue

print(min(cnt))