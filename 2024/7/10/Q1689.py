import sys
input = sys.stdin.readline


def main():
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        lst.append([s, 1])
        lst.append([e, -1])
    lst.sort()
    cnt, res = 0, 0
    for idx, v in lst:
        cnt += v
        res = max(res, cnt)
    print(res)


if __name__ == '__main__':
    main()
