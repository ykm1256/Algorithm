import sys
si = sys.stdin.readline

code = list(map(int, si().rstrip()))

dp = [0 for _ in range(len(code)+1)]
dp[0] = 1
dp[1] = 1

if code[0] == 0:
    print(0)
else:
    for i in range(1, len(code)):
        j = i + 1
        if code[i] > 0:
            dp[j] += dp[j-1]
        if 10 <= code[i] + code[i-1]*10 <= 26:
            dp[j] += dp[j-2]

    print(dp[-1] % 1000000)