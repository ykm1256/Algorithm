import sys
from bisect import bisect_left, bisect_right
si = sys.stdin.readline

N = int(si().rstrip())

students = list(map(int, si().split()))
students.sort()

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        num = students[i] + students[j]
        l = bisect_left(students, num*-1, j+1)
        r = bisect_right(students, num*-1, j+1)
        ans += r - l
print(ans)
