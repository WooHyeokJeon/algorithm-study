# 1. Test 클래스 정의
# __init__() - value를 저장 (기본값은 0)
# __call__() - 인스턴스를 함수처럼 호출하면 value에 x를 더하고 결과를 반환
class Test:
    def __init__(self, value=0):
        self.value = value

    def __call__(self, x):
        self.value += x
        return self.value

# 2. 인스턴스를 함수처럼 호출
T1 = Test(5)
print(T1(10))    # 15
print(T1(100))   # 115

# 3. 기본값(0)으로 생성한 인스턴스 호출
T2 = Test()
print(T2(10))    # 10
print(T2(100))   # 110