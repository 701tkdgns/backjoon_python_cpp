def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            bit = bin(num)[2:]
            if '0' not in bit:
                answer.append(int('10' + bit[1:], 2))
            else:
                idx = bit.rfind('0')
                bit = bit[:idx] + '10' + bit[idx + 2:]
                answer.append(int(bit, 2))
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/77885?language=python3