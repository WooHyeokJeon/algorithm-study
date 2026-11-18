# 1. A 클래스 정의
# __init__() - a, b 값을 저장
# __gt__() - > 연산자 사용 시 실행되며, 비교 결과를 "참" 또는 "거짓"으로 반환
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __gt__(self, other):
        if self.a > other.a:
            return "참"
        elif self.a == other.a and self.b > other.b:
            return "참"
        else:
            return "거짓"

# 2. 객체 생성 및 비교
ob1 = A(3, 5)
ob2 = A(50, 33)
print(ob1 > ob2)   # 거짓 (ob1.a = 3 < ob2.a = 50)