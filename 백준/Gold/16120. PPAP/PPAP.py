import sys
si = sys.stdin.readline

s = list(si().rstrip())
tmp = []
for c in s:
	tmp.append(c)
	if tmp[-4:] == ['P','P','A','P']:
		for _ in range(4):
			tmp.pop()
		tmp.append('P')

if tmp == ['P','P','A','P'] or tmp == ['P']:
	print('PPAP')
else:
	print('NP')