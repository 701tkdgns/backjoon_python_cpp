S = input()
card = {'P': [], 'K': [], 'H': [], 'T': []}
sign_lst = [13, 13, 13, 13]
chk_overlay = False
for i in range(0, len(S), +3):
    C = S[i:i + 3]
    if C[1:3] in card[C[0]]:
        chk_overlay = True
    card[C[0]].append(C[1:3])
if chk_overlay:
    print('GRESKA')
else:
    print('{} {} {} {}'.format(13 - len(card['P']), 13 - len(card['K']), 13 - len(card['H']), 13 - len(card['T'])))
