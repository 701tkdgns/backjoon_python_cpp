import random


def qs(a, l, r):
    if l < r:
        v, i, j = a[r], l - 1, r
        while True:
            i += 1
            while v > a[i]:
                i += 1
            j -= 1
            while v < a[j]:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        qs(a, l, i - 1)
        qs(a, i + 1, r)


lst = random.sample(range(100), 10)
print(lst)
qs(lst, 0, len(lst) - 1)
print(lst)
