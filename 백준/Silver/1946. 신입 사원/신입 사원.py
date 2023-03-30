import sys
si = sys.stdin.readline

# 성적 중 적어도 하나가 다른 지원자 보다 높은 사람 뽑기

T = int(si().rstrip())

for _ in range(T):
	N = int(si().rstrip())
	apply = []
	score = [0 for _ in range(N+1)]
	for _ in range(N):
		index, value = map(int, si().split())
		score[index] = value
	ans = 1
	minValue = score[1]
	for i in range(2, N+1):
		if minValue > score[i]:
			ans += 1
			minValue = min(score[i], minValue)
	print(ans)