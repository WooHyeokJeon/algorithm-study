# 1. 함수 정의
# add() - 두 수를 더한 값을 반환
def add(a, b):
    return a + b

# sub() - 두 수를 뺀 값을 반환
def sub(a, b):
    return a - b

# 2. 직접 실행했을 때만 동작
# __name__ == '__main__'은 python mod1.py로 직접 실행했을 때 True
if __name__ == '__main__':
    print(add(10, 4))   # 14
    print(sub(10, 4))   # 6