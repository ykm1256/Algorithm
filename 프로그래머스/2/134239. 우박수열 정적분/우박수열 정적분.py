def solution(k, ranges):
    answer = []
    
    pos = [[0, k]]
    x = 1
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k*3 + 1
        pos.append([x, k])
        x += 1
    
    for a, b in ranges:
        b = x-1+b
        ans = 0
        if a > b:
            ans = -1
        for i in range(a+1, b+1):
            ans += min(pos[i-1][1], pos[i][1])
            ans += abs(pos[i-1][1] - pos[i][1]) / 2
        answer.append(ans)
        
    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))