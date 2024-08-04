def move(n, atoms):
    directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    newAtoms = {}
    for (x, y) in atoms:
        for m, s, d in atoms[(x, y)]:
            nx = (x + directions[d][0] * s) % n
            ny = (y + directions[d][1] * s) % n
            if (nx, ny) in newAtoms:
                newAtoms[(nx, ny)].append((m, s, d))
            else:
                newAtoms[(nx, ny)] = [(m, s, d)]
    return newAtoms


def crash(n, atoms):
    newAtoms = {}
    for (x, y) in atoms:
        if len(atoms[(x, y)]) == 1:
            newAtoms[(x, y)] = [atoms[(x, y)][0]]
        else:
            mm, ss, dd = atoms[(x, y)][0]
            chk = True
            for m, s, d in atoms[(x, y)][1:]:
                mm += m
                ss += s
                if chk and (d % 2 != dd % 2):
                    chk = False
            mm = mm // 5
            if mm != 0:
                ss = ss // len(atoms[(x, y)])
                if chk:
                    newAtoms[(x, y)] = [(mm, ss, 0), (mm, ss, 2), (mm, ss, 4), (mm, ss, 6)]
                else:
                    newAtoms[(x, y)] = [(mm, ss, 1), (mm, ss, 3), (mm, ss, 5), (mm, ss, 7)]
    return newAtoms


def main():
    N, M, K = map(int, input().split())
    atoms = {}
    res = 0
    for _ in range(M):
        x, y, m, s, d = map(int, input().split())
        atoms[(x - 1, y - 1)] = [(m, s, d)]
    for k in range(K):
        atoms = move(N, atoms)
        atoms = crash(N, atoms)
    for (x, y) in atoms:
        for m, s, d in atoms[(x, y)]:
            res += m
    print(res)


if __name__ == "__main__":
    main()

# https://wikidocs.net/213690