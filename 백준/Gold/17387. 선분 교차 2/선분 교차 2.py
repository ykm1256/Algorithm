import sys
si = sys.stdin.readline

ans = 1

def ccw(x1,y1,x2,y2, x, y):
	return x1*y2 + x2*y +x*y1 - (x2*y1 + x*y2 + x1*y)

def isIn3(x, x1, x2):
	if (x < min(x1,x2) or x > max(x1, x2)):
		return False
	return True


x1,y1,x2,y2 = map(int, si().split())
x3,y3,x4,y4 = map(int, si().split())

ccwA = ccw(x3,y3,x4,y4,x1,y1)
ccwB = ccw(x3,y3,x4,y4,x2,y2)
ccwC = ccw(x1,y1,x2,y2,x3,y3)
ccwD = ccw(x1,y1,x2,y2,x4,y4)

if (ccwA * ccwB == 0 and ccwC*ccwD == 0):
	if (x1 == x2 and not isIn3(y3, y1, y2) and not isIn3(y4, y1, y2) and not isIn3(y1, y3, y4) and not isIn3(y2, y3, y4)):
		ans = 0
	elif (y1 == y2 and not isIn3(x3, x1, x2) and not isIn3(x4, x1, x2) and not isIn3(x1, x3, x4) and not isIn3(x2, x3, x4)):
		ans = 0
	elif (not isIn3(x3, x1, x2) and not isIn3(x4, x1, x2) and not isIn3(x1, x3, x4) and not isIn3(x2, x3, x4)):
		ans = 0
elif not (ccwA * ccwB <= 0 and ccwC * ccwD <= 0):
	ans = 0

print(ans)