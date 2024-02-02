n = int(input())
score = {1: 0, 2: 0}
_time = {1: 0, 2: 0}
res = {1: 0, 2: 0}
state = 0   # 0 : 동점, 1 : 1번팀 우세, 2 : 2번팀 우세
for _ in range(n):
    team, t = input().split()
    team = int(team)
    m, s = map(int, t.split(':'))
    t = m * 60 + s
    score[team] += 1
    if state == 0:
        _time[team] = t
        state = team
    elif state != 0 and score[1] == score[2]:
        res[state] += t - _time[state]
        state = 0
if state != 0:
    res[state] += 60 * 48 - _time[state]

print('{:0>2}:{:0>2}'.format(res[1]//60, res[1] % 60))
print('{:0>2}:{:0>2}'.format(res[2]//60, res[2] % 60))
