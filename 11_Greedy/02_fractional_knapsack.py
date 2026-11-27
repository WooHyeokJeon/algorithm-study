# 1. 분할 가능 배낭 문제 (Greedy)
def fractional_knapsack(items, capacity):
    total = 0

    # 1-1. 단위 무게당 이익이 큰 순서로 정렬
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    for weight, benefit in items:
        if capacity == 0:
            break

        # 1-2. 물건이 다 들어가면 통째로 담고, 넘치면 남은 용량만큼만 담기
        if weight <= capacity:
            total += benefit
            capacity -= weight
        else:
            total += benefit / weight * capacity
            capacity = 0

    return total


# 2. 테스트 (items: (무게, 이익))
if __name__ == "__main__":
    items = [(3, 15), (5, 20), (3, 9), (4, 14)]

    print(fractional_knapsack(items, 10))   # 42.0
    print(fractional_knapsack(items, 5))    # 23.0