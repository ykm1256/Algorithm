import sys
from collections import defaultdict
si = sys.stdin.readline

n = int(si().rstrip())

mosquito = defaultdict(int)

for _ in range(n):
	s, e = map(int, si().split())
	mosquito[s] += 1
	mosquito[e] -= 1

max_val = 0
cur_val = 0
bef_val = 0
s, e = -1, -1
flag = False

for i in sorted(mosquito.keys()):
	bef_val = cur_val
	cur_val += mosquito[i]
	if cur_val > max_val:
		max_val = cur_val
		s = i
		flag = True
	if flag and bef_val == max_val and cur_val < max_val:
		e = i
		flag = False

print(max_val)
print(s, e)