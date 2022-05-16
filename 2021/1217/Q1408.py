def second(m, c):
    res = m - c
    if res < 0:
        res += 60
        currentTime[1] = str(int(currentTime[1]) + 1)
    return res


def minute(m, c):
    res = m - c
    if res < 0:
        res += 60
        currentTime[0] = str(int(currentTime[0]) + 1)
    return res


def hour(m, c):
    res = m - c
    if res < 0:
        res += 24
    return res


currentTime = list(input().split(':'))
missionTime = list(input().split(':'))

S = second(int(missionTime[2]), int(currentTime[2]))
M = minute(int(missionTime[1]), int(currentTime[1]))
H = hour(int(missionTime[0]), int(currentTime[0]))

if H == 0:
    H = '00'
elif H < 10:
    H = '0' + str(H)
if M == 0:
    M = '00'
elif M < 10:
    M = '0' + str(M)
if S == 0:
    S = '00'
elif S < 10:
    S = '0' + str(S)
print('{}:{}:{}'.format(H, M, S))
