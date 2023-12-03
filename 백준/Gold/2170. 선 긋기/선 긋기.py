import sys
si = sys.stdin.readline

n = int(si().rstrip())

lines = []
for _ in range(n):
    lines.append(list(map(int, si().split())))

answer = 0
lines.sort()
start = lines[0][0]
end = lines[0][1]

for s, e in lines:
    if start <= s <= end:
        end = max(e, end)
    else:
        answer += end - start
        start = s
        end = e

if start != 0:
    answer += end - start
print(answer)