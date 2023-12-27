import sys
from collections import defaultdict

si = sys.stdin.readline

goal = int(si().rstrip())

m, n = map(int, si().split())

A = []
B = []
for _ in range(m):
    A.append(int(si().rstrip()))

for _ in range(n):
    B.append(int(si().rstrip()))

A_dic = defaultdict(int)
B_dic = defaultdict(int)


def sumPizza(l, pizza, pizzaDict):
    for i in range(l):
        pizzaSum = pizza[i]
        pizzaDict[pizzaSum] += 1
        for j in range(1, l-1):
            pizzaSum += pizza[(i+j) % l]
            pizzaDict[pizzaSum] += 1
    pizzaDict[0] += 1
    pizzaDict[sum(pizza)] += 1

sumPizza(m, A, A_dic)
sumPizza(n, B, B_dic)

answer = 0
for s in A_dic.keys():
    answer += A_dic[s] * B_dic[goal-s]
print(answer)