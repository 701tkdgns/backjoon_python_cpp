import sys

input = sys.stdin.readline


def findBigSum(lst):
    max_sum = 0
    if len(lst) % 2 == 0:
        for idx in range(0, len(lst), 2):
            max_sum += lst[idx] * lst[idx + 1]
    else:
        for idx in range(0, len(lst) - 1, 2):
            max_sum += lst[idx] * lst[idx + 1]
        max_sum += lst[-1]
    return max_sum


N = int(input())
positive, negative = [], []
res = 0

for _ in range(N):
    n = int(input())
    if n > 1:
        positive.append(n)
    elif n == 1:
        res += 1
    else:
        negative.append(n)
positive.sort(reverse=True)
negative.sort()
res += findBigSum(positive)
res += findBigSum(negative)

print(res)
