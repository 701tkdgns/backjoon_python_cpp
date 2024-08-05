def move(arg_atoms):
    directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    new_atoms = {}
    for x, y in arg_atoms:
        for _m, _s, _d in arg_atoms[(x, y)]:
            nx = (x + directions[_d][0] * _s + N) % N
            ny = (y + directions[_d][1] * _s + N) % N
            if (nx, ny) in new_atoms:
                new_atoms[(nx, ny)].append((_m, _s, _d))
            else:
                new_atoms[(nx, ny)] = [(_m, _s, _d)]
    return new_atoms


def crash(arg_atoms):
    new_atoms = {}
    for x, y in arg_atoms:
        if len(arg_atoms[(x, y)]) == 1:
            new_atoms[(x, y)] = [arg_atoms[(x, y)][0]]
        else:
            mm, ss, dd = arg_atoms[(x, y)][0]
            chk = True
            for _m, _s, _d in arg_atoms[(x, y)][1:]:
                mm += _m
                ss += _s
                if chk and _d % 2 != dd % 2:
                    chk = False
            mm = mm // 5
            if mm != 0:
                ss = ss // len(arg_atoms[x, y])
                if chk:
                    new_atoms[(x, y)] = {[mm, ss, 0], [mm, ss, 2], [mm, ss, 4], [mm, ss, 6]}
                else:
                    new_atoms[(x, y)] = {[mm, ss, 1], [mm, ss, 3], [mm, ss, 5], [mm, ss, 7]}

    return new_atoms


N, M, K = map(int, input().split())
atoms = {}
res = 0
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    atoms[(r - 1, c - 1)] = [(m, s, d)]
for k in range(K):
    atoms = move(atoms)
    atoms = crash(atoms)
for x, y in atoms:
    for m, s, d in atoms[(x, y)]:
        res += m
print(res)