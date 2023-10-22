import bisect, itertools
from collections import defaultdict

def solution(info, query):
    answer = []
    scores = [0 for _ in range(len(info))]
    dic = defaultdict(list)
    flags = list(itertools.product((True, False), repeat=4))

    for i in info:
        arr = i.split()
        for flag in flags:
            key = ""
            for i in range(4):
                key += arr[i] if flag[i] else '-'
            dic[key].append(int(arr[4]))
    
    for key in dic.keys():
        dic[key].sort()
    
    for q in query:
        l,_,j,_,c,_,f,s = q.split()
        s = int(s)
        key = l+j+c+f
        cnt = 0
        idx = bisect.bisect_left(dic[key], s)
        answer.append(len(dic[key]) - idx)

    return answer