import sys
from collections import deque

si = sys.stdin.readline

T = int(si().rstrip())

def cal_D(num, op):
	num = num*2
	op += "D"
	if num > 9999:
		num %= 10000
	return num,op

def cal_S(num, op):
	if num == 0:
		num = 9999
	else:
		num -= 1
	op += "S"
	return num, op

def cal_L(num,op):
	op += "L"

	if num < 1000:
		num *= 10
	else:
		tmp = num // 1000
		num = num - tmp * 1000
		num = num*10 + tmp
	return num, op

def cal_R(num,op):
	op += "R"
	tmp = num % 10
	num //= 10
	num += tmp * 1000
	return num, op


for _ in range(T):
	A, B = map(int,si().split())
	visited = [0 for _ in range(10000)]
	visited[A] = 1
	
	queue = deque()
	queue.append((A,""))
	while queue:
		now = queue.popleft()
		if now[0] == B:
			break
		if now[0] > 0:
			num, op = cal_L(now[0], now[1])
			if visited[num] == 0:
				visited[num] = 1
				queue.append((num, op))
				
			num, op = cal_R(now[0], now[1])
			if visited[num] == 0:
				visited[num] = 1
				queue.append((num,op))

			num, op = cal_D(now[0], now[1])
			if visited[num] == 0:
				visited[num] = 1
				queue.append((num, op))
		
		num, op = cal_S(now[0], now[1])
		if visited[num] == 0:
			visited[num] = 1
			queue.append((num, op))
	print(now[1])