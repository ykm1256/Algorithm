import sys
si = sys.stdin.readline

n = int(si().rstrip())
m = int(si().rstrip())

pos = list(map(int,si().split()))

l = 0
r = 2 * n
ans = r

while l <= r:
	s_light = -1
	e_light = -1
	mid = (l+r) // 2

	for i in range(m):
		if s_light == -1:
			if pos[i] - mid > 0:
				break
			s_light = 0
		else:
			if e_light < pos[i] - mid:
				break
		e_light = pos[i] + mid
	
	if e_light - s_light >= n:
		r = mid - 1
		ans = min(mid, ans)
	else:
		l = mid + 1

print(ans)