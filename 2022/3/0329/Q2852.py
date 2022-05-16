N = int(input())
a_time, b_time = 0, 0
flag = 0
for i in range(N):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    if team == '1':
        if flag == 0:
            a_time += 48 * 60 - (60 * m + s)
        flag += 1

        if flag == 0:
            if b_time > 0:
                b_time = b_time - (48 * 60 - (60 * m + s))
    else:
        if flag == 0:
            b_time += 48 * 60 - (60 * m + s)
        flag -= 1
        if flag == 0:
            if a_time > 0:
                a_time = a_time - (48 * 60 - (60 * m + s))

print('{:0>2}:{:0>2}'.format(a_time // 60, a_time % 60))
print('{:0>2}:{:0>2}'.format(b_time // 60, b_time % 60))
# 끝났을 때 무승부로 끝남
