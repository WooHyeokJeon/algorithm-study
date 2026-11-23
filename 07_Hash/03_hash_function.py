# 1. 곱셈 방법 (A는 0 < A < 1인 상수)
A = 0.6180339887

def mul_hash(x, m):
    return int(m * ((x * A) % 1))


# 2. 자릿수 접기 (문자 코드값을 더함)
def fold_hash(key, size):
    h = 0
    for ch in key:
        h += ord(ch)
    return h % size


# 3. 자릿수 접기 (왼쪽으로 3비트 이동한 뒤 더함)
def fold_shift_hash(key, size):
    h = 0
    for ch in key:
        h = (h << 3) + ord(ch)
    return h % size


# 4. 테스트
if __name__ == "__main__":
    print(mul_hash(1, 10))   # 6
    print(mul_hash(2, 10))   # 2
    print(mul_hash(3, 10))   # 8

    print(fold_hash("Hello", 1000))   # 500
    print(fold_shift_hash("Hello", 12289))   # 10419