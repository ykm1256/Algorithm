from collections import deque

def solution(queue1, queue2):
    q1 = deque()
    q2 = deque()
    sum1 = 0
    sum2 = 0
    for i in range(len(queue1)):
        sum1 += queue1[i]
        sum2 += queue2[i]
        q1.append(queue1[i])
        q2.append(queue2[i])

    limit = len(queue1) + 10

    p1 = 0
    p2 = 0

    while p1 < limit and p2 < limit:
        if sum1 < sum2:
            num = q2.popleft()
            sum1 += num
            sum2 -= num
            q1.append(num)
            p1 += 1
        elif sum1 > sum2:
            num = q1.popleft()
            sum1 -= num
            sum2 += num
            q2.append(num)
            p2 += 1
        else:
            return p1 + p2
    return -1

