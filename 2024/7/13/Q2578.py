import sys
input = sys.stdin.readline

def vertical(visit):
    cnt = 0
    for row in visit:
        if sum(row) == 5:
            cnt += 1
    return cnt

def horizon(visit):
    cnt = 0
    for col in visit:
        if sum(col) == 5:
            cnt += 1
    return cnt

def diagonal_left(visit):
    cnt, tmp = 0, 0
    for idx in range(5):
        tmp += visit[idx][idx]
    if tmp == 5:
        cnt = 1
    return cnt

def diagonal_right(visit):
    cnt, tmp = 0, 0
    for idx in range(5):
        tmp += visit[idx][4 - idx]
    if tmp == 5:
        cnt = 1
    return cnt

def bingo(chk, cnt):
    for col in range(5):
        for row in range(5):
            if chk == board[col][row]:
                visit[col][row] = 1
                cnt1 = vertical(visit)
                cnt2 = horizon(visit)
                cnt3 = diagonal_right(visit)
                cnt4 = diagonal_left(visit)
                if cnt1 + cnt2 + cnt3 + cnt4 >= 3:
                    print(cnt)
                    return True


board, people = [], []
visit = [[0 for _ in range(5)] for _ in range(5)]
for _ in range(5):
    tmp = list(map(int, input().split()))
    board.append(tmp)
for _ in range(5):
    tmp = list(map(int, input().split()))
    people.append(tmp)
cnt = 0
res = False
for c in range(5):
    for r in range(5):
        cnt += 1
        chk = people[c][r]
        res = bingo(chk, cnt)
        if res:
            break
    if res:
        break