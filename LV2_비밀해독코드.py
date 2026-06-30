from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    candidates = combinations(range(1, n + 1), 5)

    for candidate in candidates:
        possible = True

        for i in range(len(q)):

            cnt = len(set(candidate) & set(q[i]))

            if cnt != ans[i]:
                possible = False
                break

        if possible:
            answer += 1

    return answer
