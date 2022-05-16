T = int(input())
for _ in range(T):
    word_cnt = int(input())
    fir_public_key = input().split()
    sec_public_key = input().split()
    txt = input().split()
    res = ['' for _ in range(word_cnt)]
    f_lst, s_lst = [i for i in range(word_cnt)], []

    for i in range(len(fir_public_key)):
        for j in range(len(sec_public_key)):
            if fir_public_key[i] == sec_public_key[j]:
                s_lst.append(j)
                break

    for i in range(len(txt)):
        res[i] = txt[s_lst[f_lst[i]]]

    for i in res:
        print(i, end=' ')