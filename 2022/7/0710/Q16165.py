import sys

std = sys.stdin

N, M = map(int, std.readline().split())
girl_group = {}
for _ in range(N):
    group_name = std.readline().rstrip()
    member_cnt = int(std.readline().rstrip())
    tmp = []
    for _ in range(member_cnt):
        tmp.append(std.readline().rstrip())
    tmp.sort()
    girl_group[group_name] = tmp

for _ in range(M):
    answer = std.readline().rstrip()
    check = int(std.readline().rstrip())
    if check:
        for key in girl_group:
            if answer in girl_group[key]:
                print(key)
                break
    else:
        for lst in girl_group[answer]:
            print(lst)
