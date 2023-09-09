import sys
si = sys.stdin.readline

n = int(si().rstrip())
s = si().rstrip()
w = 0
h = 0
e = 0
ans = 0
for c in s:
	if c == 'W':
		w += 1
	elif c == 'H':
		h += w
	elif c == 'E':
		ans = 2*ans + e
		e += h
print(ans % 1000000007)