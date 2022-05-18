def solution(lottos, win_nums):
    cnt_z, cnt_correct = 0, 0
    ranking = [6, 6, 5, 4, 3, 2, 1]
    for num in lottos:
        if num == 0:
            cnt_z += 1
        elif num in win_nums:
            cnt_correct += 1
    best, worst = cnt_correct + cnt_z, cnt_correct

    answer = [ranking[best], ranking[worst]]

    return answer