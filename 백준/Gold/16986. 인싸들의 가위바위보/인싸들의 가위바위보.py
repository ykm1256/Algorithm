import sys
si = sys.stdin.readline

N,K = map(int, si().split())
arr = [[0 for _ in range(N+1)]]
for i in range(1, N+1):
    arr.append([0])
    arr[i].extend(list(map(int, si().split())))

kyung = list(map(int, si().split()))
minho = list(map(int, si().split()))
next = [0, 2, 1, 0]

chk = [0 for _ in range(N+1)]
wins = [0, 0, 0]

route = [0 for _ in range(20)]

def recur(a, b, idx_k, idx_m, depth):
    global N, K

    if a != 0:
        a_val = kyung[idx_k]
        b_val = minho[idx_m]

        if arr[a_val][b_val] == 2:
            na = a
        else:
            na = b
        wins[na] += 1
        if wins[na] >= K:
            wins[na] -= 1
            return
        recur(0, na, idx_k+1, idx_m+1, depth+1)
        wins[na] -= 1

    else:
        b_val = kyung[idx_k] if b == 1 else minho[idx_m]
        for a_val in range(1, N+1):
            if chk[a_val] == 1:
                continue
            chk[a_val] = 1
            if arr[a_val][b_val] == 2:
                na = a
            else:
                na = b
            wins[na] += 1
            if wins[na] >= K:
                if na == 0:
                    print(1)
                    exit()
                wins[na] -= 1
                chk[a_val] = 0
                continue
            route[depth] = a_val
            tmp = na
            na = min(na, next[a+b])
            nb = max(tmp, next[a+b])
            if b == 1:
                recur(na, nb, idx_k+1, idx_m, depth+1)
            else:
                recur(na, nb, idx_k, idx_m+1, depth+1)
            wins[tmp] -= 1
            chk[a_val] = 0

recur(0, 1, 0, 0,0)
print(0)