import sys
si = sys.stdin.readline

n, s = map(int, si().split())

nums = list(map(int, si().split()))

ans = 0


def recur(idx, num, cnt):
    global s, ans, n
    if idx >= n:
        return

    recur(idx+1, num, cnt)
    # 더해질 때만 체크?
    if num+nums[idx] == s:
        ans += 1
    recur(idx+1, num+nums[idx], cnt+1)

recur(0, 0, 0)
print(ans)