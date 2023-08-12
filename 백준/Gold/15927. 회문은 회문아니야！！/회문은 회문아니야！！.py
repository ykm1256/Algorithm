import sys
from collections import deque
si = sys.stdin.readline

def allCoincide(str):
	for i in range(len(str)-1):
		if str[i] != str[i+1]:
			return False
	return True

def isPalin(str):
	l = len(str)

	for i in range(l//2):
		if str[i] != str[l-i-1]:
			return False
	return True

input = si().rstrip()

if allCoincide(input):
	print(-1)
elif isPalin(input):
	print(len(input) - 1)
else:
	print(len(input))