import sys

input = sys.stdin.readline


def room():
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append([a, b])
    lst.sort(key=lambda x: (x[1], x[0]))
    end_idx, cnt = 0, 0
    for s, e in lst:
        if s >= end_idx:
            end_idx = e
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    room()
