import sys

si = sys.stdin.readline

C = int(si().rstrip())

def recur(node, result):
    global answer
    if node == 12:
        answer = max(answer, result)
        return

    for i in range(11):
        if position[i] != 0 or stats[node][i] == 0:
            continue
        position[i] = node
        recur(node+1, result+stats[node][i])
        position[i] = 0
    
for _ in range(C):
    answer = 0
    stats = [[]]
    for _ in range(11):
        stats.append(list(map(int, si().split())))
    
    chk = [0 for _ in range(12)]
    position = [0 for _ in range(11)]

    
    recur(1, 0)
    print(answer)