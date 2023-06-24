import sys

si = sys.stdin.readline

N = int(si().rstrip())
apples = list(map(int, si().split()))
apple_sum = sum(apples)
ans = 'YES'
turn = apple_sum // 3

if apple_sum % 3 != 0:
	ans = 'NO'
else:
	for apple in apples:
		turn -= apple // 2
	
	if turn > 0:
		ans = 'NO'
print(ans)