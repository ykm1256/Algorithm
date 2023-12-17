import heapq

def solution(N, road, K):
    answer = 0
    
    times = [float('inf') for _ in range(N)]
    tree = [[0 for _ in range(N)] for _ in range(N)]
    times[0] = 0
    
    for a,b,c in road:
        tree[a-1][b-1] = c if tree[a-1][b-1] == 0 else min(tree[a-1][b-1], c)
        tree[b-1][a-1] = c if tree[b-1][a-1] == 0 else min(tree[b-1][a-1], c)
    queue = []
    heapq.heappush(queue, (0,0))
    while queue:
        t, node = heapq.heappop(queue)
        for next in range(N):
            dt = t + tree[node][next]
            if tree[node][next] == 0 or times[next] <= dt:
                continue
            times[next] = dt
            heapq.heappush(queue, (dt, next))
    
    for i in range(N):
        if times[i] <= K:
            answer += 1

    return answer

N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3

solution(N,road,K)