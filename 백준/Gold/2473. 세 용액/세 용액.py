import sys
si = sys.stdin.readline

n = int(si().rstrip())

l = list(map(int, si().split()))

value = sys.maxsize

l.sort()

ans = [0,0,0]


for i in range(n-2):
    s = i+1
    e = n-1
    while s < e:
        res = l[i] + l[s] + l[e]
        if abs(res) < value:
            value = abs(res)
            ans = [l[i],l[s],l[e]]
        if res < 0:
            s += 1
        elif res > 0:
            e -= 1
        else:
            break

print(*ans)