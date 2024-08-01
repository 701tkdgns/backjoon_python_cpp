n, m = map(int, input().split())  # 명단 수 / 친구 수
N = list(map(int, input().split()))
M = list(map(int, input().split()))
cnt = 0
for i in range(m):
    if N[i] not in M:
        cnt += 1
print(cnt)
