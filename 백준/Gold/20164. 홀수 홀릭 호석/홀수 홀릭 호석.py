import sys
si = sys.stdin.readline

N = si().rstrip()

ansMin = float('inf')
ansMax = 0

def countOdd(num):
    ans = 0
    for c in num:
        if int(c) % 2 == 1:
            ans += 1
    return ans

def recur(num, cnt):
    global ansMin, ansMax
    cnt += countOdd(num)
    l = len(num)
    if l == 1:
        ansMax = max(cnt, ansMax)
        ansMin = min(cnt, ansMin)
        return
    
    elif l == 2:
        recur(str(int(num[0]) + int(num[1])), cnt)
    else:
        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    res = int(num[i:j]) + int(num[j:k]) + int(num[k:])
                    recur(str(res), cnt)

recur(N, 0)
print(ansMin, ansMax)