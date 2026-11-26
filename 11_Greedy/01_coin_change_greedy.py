# 1. 거스름돈 최소 개수 만들기 (Greedy)
def min_coin(coins, change):
    res = []

    # 1-1. 단위가 큰 동전부터 가능한 만큼 선택
    for coin in sorted(coins, reverse=True):
        while change >= coin:
            res.append(coin)
            change -= coin

    return res


# 2. 테스트
if __name__ == "__main__":
    print(min_coin([500, 100, 50, 10], 800))   # [500, 100, 100, 100]
    print(min_coin([500, 400, 100, 50, 10], 800))   # [500, 100, 100, 100] (최적은 [400, 400])