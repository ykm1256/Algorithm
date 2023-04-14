import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

a, b = map(int, si().split())
answer = -1

def recur(cnt, num):
	global answer
	if num <= a:
		if a == num:
			if answer == -1:
				answer = cnt
			else:
				answer = min(answer, cnt)
		return
	
	if num % 2 == 1 and num % 10 != 1:
		return
	
	if num % 10 == 1:
		recur(cnt+1, num//10)
	else:
		recur(cnt+1, num//2)

recur(1, b)
print(answer)