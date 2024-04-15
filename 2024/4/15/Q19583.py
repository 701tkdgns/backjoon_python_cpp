import sys
input = sys.stdin.readline

chk = dict()
S, E, Q = input().split()
S_HH, S_MM = S.split(':')
E_HH, E_MM = E.split(':')
Q_HH, Q_MM = Q.split(':')
while True:
    try:
        logTime, who = input().split()
        log_HH, log_MM = logTime.split(':')
        if log_HH < S_HH:
            chk[who] = chk.get(who, 0) + 1
        elif log_HH == S_HH and log_MM == S_MM:
            chk[who] = chk.get(who, 0) + 1
        elif E_HH <= log_HH < Q_HH:
            chk[who] = chk.get(who, 0) + 2
        elif E_HH == log_HH == Q_HH and E_MM <= log_MM <= Q_MM:
            chk[who] = chk.get(who, 0) + 2
        elif Q_HH == log_HH and Q_MM == log_MM:
            chk[who] = chk.get(who, 0) + 2
    except:
        break
keys = chk.keys()
res = 0
for key in keys:
    if chk[key] >= 3:
        res += 1
print(res)
