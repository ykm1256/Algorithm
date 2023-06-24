import sys
si = sys.stdin.readline

N = int(si().rstrip())

flowers = []
ans = []
for _ in range(N):
	flowers.append(list(map(int,si().split())))
flowers.sort()

month = 3
day = 1
flag = False

for f in flowers:
	if flag:
		prev = ans[-1]
	else:
		if f[2] < month or (f[2] == month and f[3] <= day):
			continue
		if f[0] > month or (f[0] == month and f[1] > day):
			continue
		ans.append(f)
		flag = True
		if ans[-1][2] == 12:
			break
		continue

	if f[0] > month or (f[0] == month and f[1] > day):
		if not flag:
			ans = []
			break
		month = prev[2]
		day = prev[3]
		flag = False
		
		if f[0] > month or (f[0] == month and f[1] > day):
			ans = []
			break
		if f[2] > month or (f[2] == month and f[3] > day):
			ans.append(f)
			flag = True
	else:
		if (prev[2] < f[2] or (prev[2] == f[2] and prev[3] < f[3])):
			ans.pop()
			ans.append(f)
	
	if ans[-1][2] == 12:
		break
if ans and ans[-1][2] < 12:
	ans = []

print(len(ans))