import sys
si = sys.stdin.readline

n = int(si().rstrip())

snow = list(map(int, si().split()))

snow.sort()

answer = float('inf')
for i in range(n-3):
	for j in range(i+3, n):
		l = i+1
		r = j-1

		while(l < r):
			a = snow[i] + snow[j]
			e = snow[l] + snow[r]
			result = abs(a - e)
			answer = min(answer, result)
		
			if a < e:
				r -= 1
			else:
				l += 1

print(answer)