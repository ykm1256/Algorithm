import sys
si = sys.stdin.readline

# 완전 이진 트리
k = int(si().rstrip())
order = list(map(int, si().split()))
tree = [[] for _ in range(k)]

idx = 0

def recur(depth):
    global k, idx
    if idx >= len(order):
        return
    
    if depth < k-1:
        recur(depth+1)
    tree[depth].append(order[idx])
    idx += 1
    if depth < k-1:
        recur(depth+1)

recur(0)
for i in range(k):
    print(*(tree[i]))