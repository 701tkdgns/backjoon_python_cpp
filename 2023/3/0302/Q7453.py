n = int(input())
lst = []
ab, cd = [], []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        ab.append(lst[i][0] + lst[j][1])
        cd.append(lst[i][2] + lst[j][3])
ab.sort()
cd.sort()
i, j = 0, len(ab) - 1
res = 0
while i < len(ab) and j >= 0:
    if ab[i] + cd[j] == 0:
        next_i, next_j = i + 1, j - 1
        while next_i < len(ab) and ab[next_i] == ab[i]:
            next_i += 1
        while next_j >= 0 and cd[next_j] == cd[j]:
            next_j -= 1
        res += (next_i - i) * (j - next_j)
        i, j = next_i, next_j
    elif ab[i] + cd[j] > 0:
        j -= 1
    else:
        i += 1
print(res)

# n = int(input())
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
# ab, cd = [], []
# for i in range(n):
#     for j in range(n):
#         ab.append(data[i][0] + data[j][1])
#         cd.append(data[i][2] + data[j][3])
#
# ab.sort()
# cd.sort()
# i, j = 0, len(cd) - 1
# res = 0
# while i < len(ab) and j >= 0:
#     if ab[i] + cd[j] == 0:
#         next_i, next_j = i + 1, j - 1
#         while next_i < len(ab) and ab[i] == ab[next_i]:
#             next_i += 1
#         while next_j >= 0 and cd[j] == cd[next_j]:
#             next_j -= 1
#         res += (next_i - i) * (j - next_j)
#         i, j = next_i, next_j
#     elif ab[i] + cd[j] > 0:
#         j -= 1
#     else:
#         i += 1
# print(res)
