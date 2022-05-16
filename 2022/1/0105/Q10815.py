import sys


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == sgList[mid]:
            return mid
        elif sgList[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(sys.stdin.readline())
sgList = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split()))
sgList.sort()

for i in range(M):
    if binary_search(cardList[i], 0, N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
