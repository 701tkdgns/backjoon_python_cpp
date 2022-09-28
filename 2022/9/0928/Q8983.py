M, N, L = map(int, input().split())  # 사대 수, 동물 수, 사정거리
M_list = list(map(int, input().split()))
animal_list = []
visit = [False for _ in range(N)]
res = 0

M_list.sort(reverse=True)

for _ in range(N):
    x, y = map(int, input().split())
    animal_list.append([x, y])

animal_list.sort(key=lambda x: (-x[1]))

# low, high = 0,

print(res)
