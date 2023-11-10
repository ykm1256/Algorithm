from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_cnt = defaultdict(int)
    genre_map = defaultdict(list)

    for i in range(len(genres)):
        genre_cnt[genres[i]] += plays[i]
        genre_map[genres[i]].append((plays[i], -i))
    
    cnts = []
    for key in genre_cnt.keys():
        cnts.append((genre_cnt[key], key))
    cnts.sort(reverse=True)

    for i in range(len(cnts)):
        genre = cnts[i][1]
        arr = genre_map[genre]
        arr.sort(reverse=True)
        for j in range(min(len(arr), 2)):
            answer.append(-arr[j][1])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)