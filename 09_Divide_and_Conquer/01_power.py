# 1. 거듭제곱 계산 (분할정복)
def power(base, exp):
    if exp == 1:
        return base

    if exp == 0:
        return 1

    base2 = power(base, exp // 2)

    if exp % 2 == 0:
        return base2 * base2
    else:
        return base2 * base2 * base


# 2. 테스트
if __name__ == "__main__":
    print(power(5, 12))   # 244140625
    print(power(5, 19))   # 19073486328125