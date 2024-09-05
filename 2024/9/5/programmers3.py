from collections import Counter


def solution(genres, plays):
    answer, pl = [], []
    gm = dict()
    gm2 = dict()
    for i in range(len(genres)):
        gm[genres[i]] = gm.get(genres[i], 0) + plays[i]
        gm2[genres[i]] = gm2.get(genres[i], 0)
    for i in range(len(genres)):
        pl.append([gm[genres[i]], plays[i], i])
    pl.sort(key=lambda x: (-x[0], -x[1], x[2]))
    for cnt, p, idx in pl:
        if gm2[genres[idx]] < 2:
            gm2[genres[idx]] = gm2.get(genres[idx], 0) + 1
            answer.append(idx)

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=cpp