import sys, bisect
si = sys.stdin.readline


t = int(si().rstrip())

for _ in range(t):
	answer = "YES"
	n = int(si().rstrip())
	
	numbers = []
	for _ in range(n):
		numbers.append(si().rstrip())
	
	numbers.sort()
	for i in range(n-1,-1,-1):
		num = numbers[i]
		res = ""
		for idx in range(len(num)):
			res += num[idx]

			pos = bisect.bisect_left(numbers, res)
			
			if pos < n and numbers[pos] == res and res != numbers[i]:
				answer = "NO"
				break

		if answer == "NO":
			break
	print(answer)		
