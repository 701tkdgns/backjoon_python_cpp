import sys

input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        lst = []
        for _ in range(N):
            a, b = map(int, input().split())
            lst.append([a, b])
        lst.sort()
        cnt, good = 1, lst[0][1]
        for i in range(1, N):
            if lst[i][1] < good:
                good = lst[i][1]
                cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
