def solution(players, m, k):
    answer = 0
    setting = [0] * k
    for i in range(len(players)):
        needed = players[i] // m
        setting.pop(0)
        
        if needed > sum(setting):
            setting.append(needed-sum(setting))
        else:
            setting.append(0)
        print(setting)
        answer = answer + setting[-1]
    return answer
#뭐 때문에 틀렸던 건지 모르겠지만 코드를 처음부터 다시 만드니까 성공했다
#뇌에서는 분명히 맞는데 안될 때는 처음부터 해보는 것도 좋은 방법인 듯하다
