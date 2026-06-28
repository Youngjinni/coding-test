def solution(wallet, bill):
    answer = 0
    while True:
        wallet_min = min(wallet)
        wallet_max = max(wallet)
        bill_min = min(bill)
        bill_max = max(bill)
        if bill_min > wallet_min or wallet_max < bill_max:
            bill = [bill_min, int(bill_max/2)]
            answer = answer + 1
            print(bill)
        else:
            break
    return answer
#전체적으로 쉬웠던 문제다.
#max와 min함수를 알면 문제에서 제시한 로직보다 간단하게 구현 가능했다.
