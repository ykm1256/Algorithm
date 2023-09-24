import sys
si = sys.stdin.readline

a, b = map(int, si().split())
cnts = [0 for _ in range(60)]

def count_one(num):
    cnt = 0
    num_bin = bin(num)[2:]
    l = len(num_bin)

    for i in range(l):
        if num_bin[i] == '1':
            val = l - i -1
            cnt += cnts[val]
            cnt += num - (2**val) + 1
            num = num - (2**val)
    return cnt

for i in range(1, 60):
    cnts[i] = 2**(i-1) + 2 * cnts[i-1]

print(count_one(b) - count_one(a-1))