from itertools import product

def solution(users, emoticons):
    max_cnt = 0
    max_price = 0
    l = len(emoticons)
    for sale in product([10,20,30,40], repeat=l):
        sum_price = 0
        sum_cnt = 0
        for user in users:
            price = 0
            for i in range(l):
                if sale[i] >= user[0]:
                    price += (emoticons[i] * (100 - sale[i]))//100
            if price >= user[1]:
                price = 0
                sum_cnt += 1
            sum_price += price
        if max_cnt < sum_cnt:
            max_cnt = sum_cnt
            max_price = sum_price
        elif max_cnt == sum_cnt:
            max_price = max(max_price, sum_price)

    return [max_cnt, max_price]