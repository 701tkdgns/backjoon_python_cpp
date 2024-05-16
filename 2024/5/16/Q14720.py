N = int(input())
lst = list(map(int, input().split())) # 0 딸기 1 초코 2 바나나
# 로직 : 딸기 > 초코 > 바나나 > 딸기 ...
cnt = 0
for i in range(N):
    if lst[i] == cnt % 3:
        cnt += 1
print(cnt)
