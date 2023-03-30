import sys
si = sys.stdin.readline


N = int(si().rstrip())
crain = list(map(int, si().split()))
crain.sort()
M = int(si().rstrip())
box = list(map(int,si().split()))
box.sort()


ans = 0
if box[-1] > crain[-1]:
    box = []
    ans = -1
while box:
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if box[0] > crain[i]:
                break
            if box[j] <= crain[i]:
                del box[j]
                M -= 1
                break
    ans += 1
print(ans)