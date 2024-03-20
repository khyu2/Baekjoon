def solution(genres, plays):
    answer = []
    total = {}
    a = list(enumerate(zip(genres, plays)))
    a.sort(reverse=True, key=lambda x: x[1])
    
    for key, val in zip(genres, plays):
        if key not in total: total[key] = val
        else: total[key] += val
    
    tmp = sorted(list(total.items()), reverse=True, key=lambda x: x[1])
    
    for gen, pl in tmp:
        cnt = 0
        for idx, x in a:
            if x[0] == gen:
                answer.append(idx)
                cnt += 1
            if cnt == 2: break

    return answer