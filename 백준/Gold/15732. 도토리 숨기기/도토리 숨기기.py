import sys
si = sys.stdin.readline

n,k,d = map(int, si().split())

a = []
b = []
c = []

for _ in range(k):
	A,B,C = map(int, si().split())
	a.append(A)
	b.append(B)
	c.append(C)

def cal(box):
	global k, d
	cnt = 0
	for i in range(k):
		if box < a[i]:
			continue
		cnt += (min(b[i], box) - a[i]) // c[i] + 1
	
	return cnt >= d

low = 1
high = 1000000
while (low <= high):
	mid = (low+high)//2
	if (cal(mid)):
		high = mid - 1
	else:
		low = mid + 1

print(low)