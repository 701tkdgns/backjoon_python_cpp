M, N, L = map(int, input().split())  # 사대 수, 동물 수, 사정거리
M_list = list(map(int, input().split()))
animal_list = []
visit = [False for _ in range(N)]
res = 0

M_list.sort()
for _ in range(N):
    x, y = map(int, input().split())
    animal_list.append([x, y])

for a, b in animal_list:
    start, end = 0, len(M_list) - 1
    while start < end:
        mid = (start+end) // 2
        if M_list[mid] < a:
            start = mid + 1
        else:
            end = mid
    if abs(M_list[end]-a)+b <= L or abs(M_list[end-1]-a)+b <= L:
        res += 1
print(res)