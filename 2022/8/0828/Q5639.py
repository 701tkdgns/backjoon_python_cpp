import sys

sys.setrecursionlimit(100000)


def tree(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if lst[start] < lst[i]:
            mid = i
            break
    tree(start + 1, mid - 1)
    tree(mid, end)
    print(lst[start])


lst = []
while True:
    try:
        a = int(input())
        lst.append(a)
    except:
        break
tree(0, len(lst) - 1)
