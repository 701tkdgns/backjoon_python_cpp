import random


def qsort(a):
    if len(a) <= 1:
        return a

    left, right = list(), list()
    pivot = a[0]
    for i in range(1, len(a)):
        if pivot > a[i]:
            left.append(a[i])
        else:
            right.append(a[i])
    return qsort(left) + [pivot] + qsort(right)


lst = random.sample(range(100), 10)
print(lst)
res = qsort(lst)
print(res)
