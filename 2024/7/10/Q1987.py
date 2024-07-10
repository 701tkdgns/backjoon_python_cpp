import sys

input = sys.stdin.readline


def alphabet(x, y, s, direct, r, c, lst):
    res = len(s)
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if lst[nx][ny] not in s:
                res = max(res, alphabet(nx, ny, s + lst[nx][ny], direct, r, c, lst))
    return res


def main():
    r, c = map(int, input().split())
    lst = []
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for _ in range(r):
        tmp = list(map(str, input().rstrip()))
        lst.append(tmp)
    res = alphabet(0, 0, lst[0][0], direction, r, c, lst)
    print(res)


if __name__ == "__main__":
    main()
