def check(string):
	l = len(string)
	for s_idx in range(l):
		if string[s_idx] == sign[0]:
			for e_idx in range(s_idx, l):
				if string[e_idx] == sign[-1]:
					avg = (e_idx - s_idx) // (len(sign) - 1)
					cnt = 0
					while cnt < len(sign):
						if string[s_idx + avg * cnt] == sign[cnt]:
							cnt += 1
							continue
						break
					else:
						return 1
	return 0

N = int(input())
sign = input()
lst = []
res = 0
for _ in range(N):
	lst.append(input())
for old_sign in lst:
	res += check(old_sign)
print(res)