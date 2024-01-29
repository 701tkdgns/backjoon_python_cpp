# import sys
#
#
# def back_tracking(cnt, idx):
#     # 암호를 만들었을 때
#     if cnt == l:
#         # 모음, 자음 체크
#         vo, co = 0, 0
#
#         for i in range(l):
#             if answer[i] in consonant:
#                 vo += 1
#             else:
#                 co += 1
#
#         # 모음 1개 이상, 자음 2개 이상
#         if vo >= 1 and co >= 2:
#             print("".join(answer))
#
#         return
#
#     # 반복문을 통해 암호를 만든다.
#     for i in range(idx, c):
#         answer.append(words[i])
#         back_tracking(cnt + 1, i + 1) # 백트래킹
#         answer.pop()
#
#
# l, c = map(int, sys.stdin.readline().split())
# words = sorted(list(map(str, sys.stdin.readline().split())))
# consonant = ['a', 'e', 'i', 'o', 'u']
# answer = []
# back_tracking(0, 0)


def dfs(tmp):
    if len(tmp) == L:
        _tmp = ''
        a, b = 0, 0
        for _i in tmp:
            if chr(_i) in 'aeiou':
                a += 1
            else:
                b += 1
            _tmp += chr(_i)
        if a >= 1 and b >= 2:
            res.append(_tmp)
        return
    for _i in range(C):
        if tmp:
            if tmp[-1] < idx_lst[_i]:
                tmp.append(idx_lst[_i])
                dfs(tmp)
                tmp.remove(idx_lst[_i])
        else:
            tmp.append(idx_lst[_i])
            dfs(tmp)
            tmp.remove(idx_lst[_i])


L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
idx_lst = []
res = []
for c in lst:
    idx_lst.append(ord(c))
dfs([])
for i in res:
    print(i)
