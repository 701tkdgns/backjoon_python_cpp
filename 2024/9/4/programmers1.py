def solution(n, s):
    if s < n: return [-1]
    q, r = divmod(s, n)
    answer = [q] * n
    for i in range(r):
        answer[i] += 1
    answer.sort()
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/12938?language=python3